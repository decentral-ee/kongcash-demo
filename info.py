"""
Device Info Retrieval Example
"""
# (c) 2015-2018 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE. IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT,
# SPECIAL, PUNITIVE, INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE
# OF ANY KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF
# MICROCHIP HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE
# FORESEEABLE. TO THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL
# LIABILITY ON ALL CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED
# THE AMOUNT OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR
# THIS SOFTWARE.

from cryptoauthlib import *
from common import *


def info(iface='hid', device='ecc', **kwargs):
    ATCA_SUCCESS = 0x00

    # Loading cryptoauthlib(python specific)
    load_cryptoauthlib()

    # Get the target default config
    cfgfn = 'cfg_at{}a_{}_default'.format(atca_names_map.get(device), atca_names_map.get(iface))
    print("cfgfn", cfgfn)
    cfg = eval(cfgfn + "()")

    # Set interface parameters
    if kwargs is not None:
        for k, v in kwargs.items():
            icfg = getattr(cfg.cfg, 'atca{}'.format(iface))
            setattr(icfg, k, int(v, 16))

    # hard code for raspberry pi
    #cfg.cfg.atcai2c.bus = 1
    #cfg.cfg.atcai2c.slave_address = 0x60
    #cfg.cfg.atcai2c.baud = 50000
    #print("cfg.cfg.iface_type", cfg.cfg.iface_type)
    #cfg.wake_delay = 2560
    #cfg.rx_retries = 1000
    print("cfg.iface_type", cfg.iface_type)
    print("cfg.devtype", cfg.devtype)
    print("cfg.wake_delay", cfg.wake_delay)
    print("cfg.rx_retries", cfg.rx_retries)
    print("cfg.cfg.atcai2c.bus", cfg.cfg.atcai2c.bus)
    print("cfg.cfg.atcai2c.slave_address", cfg.cfg.atcai2c.slave_address)
    print("cfg.cfg.atcai2c.baud", cfg.cfg.atcai2c.baud)

    # Initialize the stack
    status = atcab_init(cfg)
    print('atcab_init status', status)
    assert status == ATCA_SUCCESS

    # Request the Revision Number
    info = bytearray(4)
    status = atcab_info(info)
    #print('atcab_info status', status)
    assert status == ATCA_SUCCESS
    print('\nDevice Part:')
    print('    ' + get_device_name(info))

    # Request the Serial Number
    serial_number = bytearray(9)
    status = atcab_read_serial_number(serial_number)
    #print("atcab_read_serial_number status", status)
    assert status == ATCA_SUCCESS
    print('\nSerial number: ')
    print(pretty_print_hex(serial_number, indent='    '))

    # Read the configuration zone
    config_zone = bytearray(128)
    assert atcab_read_config_zone(config_zone) == ATCA_SUCCESS

    print('\nConfiguration Zone:')
    print(pretty_print_hex(config_zone, indent='    '))

    # Check the device locks
    print('\nCheck Device Locks')
    is_locked = AtcaReference(False)
    assert atcab_is_locked(0, is_locked) == ATCA_SUCCESS
    config_zone_locked = bool(is_locked.value)
    print('    Config Zone is %s' % ('locked' if config_zone_locked else 'unlocked'))

    assert atcab_is_locked(1, is_locked) == ATCA_SUCCESS
    data_zone_locked = bool(is_locked.value)
    print('    Data Zone is %s' % ('locked' if data_zone_locked else 'unlocked'))

    # Load the public key
    if data_zone_locked:
        print('\nLoading Public key\n')
        for i in range(0, 16):
            public_key = bytearray(64)
            status = atcab_read_pubkey(i, public_key)
            #assert status == ATCA_SUCCESS
            if status == ATCA_SUCCESS and not public_key == b"\xff"*64:
                print("atcab_read_pubkey slot", i, public_key)
                print(convert_ec_pub_to_pem(public_key))

    # Free the library
    atcab_release()


if __name__ == '__main__':
    parser = setup_example_runner(__file__)
    args = parser.parse_args()

    info(args.iface, args.device, **parse_interface_params(args.params))
    print('\nDone')
