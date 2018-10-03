from helpers.color import gre, red, yel, cyan


def summary(i, region_name: str=''):
    try:
        print()
        print("Id: {0}\tRegion: {1}\tState: {2}\tLaunched: {3}".format(
            cyan(i.id),
            yel(region_name),
            gre(i.state['Name']),
            cyan(i.launch_time),
        ))

        print("\tArch: {0}\tHypervisor: {1}\tRoot Device Name: {2}".format(
            cyan(i.architecture),
            cyan(i.hypervisor),
            cyan(i.root_device_name)
        ))

        print("\tPriv. IP: {0}\tPub. IP: {1}".format(
            red(i.private_ip_address),
            gre(i.public_ip_address)
        ))

        print("\tPriv. DNS: {0}\tPub. DNS: {1}".format(
            red(i.private_dns_name),
            gre(i.public_dns_name)
        ))

        print("\tSubnet: {0}\tSubnet Id: {1}".format(
            cyan(i.subnet),
            cyan(i.subnet_id)
        ))

        print("\tKernel: {0}\tInstance Type: {1}".format(
            cyan(i.kernel_id),
            cyan(i.instance_type)
        ))

        print("\tRAM Disk Id: {0}\tAMI Id: {1}\tPlatform: {2}\t EBS Optimized: {3}".format(
            cyan(i.ramdisk_id),
            cyan(i.image_id),
            cyan(i.platform),
            cyan(i.ebs_optimized)
        ))

        print("\tBlock Device Mappings:")
        for idx, dev in enumerate(i.block_device_mappings, start=1):
            print("\t- [{0}] Device Name: {1}\tVol Id: {2}\tStatus: {3}\tDeleteOnTermination: {4}\tAttachTime: {5}".format(
                idx,
                cyan(dev['DeviceName']),
                cyan(dev['Ebs']['VolumeId']),
                cyan(dev['Ebs']['Status']),
                cyan(dev['Ebs']['DeleteOnTermination']),
                cyan(dev['Ebs']['AttachTime'])
            ))

        print("\tTags:")
        for tag in i.tags:
            print("\t- {0}: {1}".format(
                cyan(tag['Key']),
                cyan(tag['Value'])
            ))

        print("\tProduct codes:")
        for idx, details in enumerate(i.product_codes, start=1):
            print("\t - [{0}] Id: {1}\tType: {2}".format(
                idx,
                cyan(details['ProductCodeId']),
                cyan(details['ProductCodeType'])
            ))

        print("Console Output:")
        # Commented out because this creates a lot of clutter..
        # print(i.console_output()['Output'])
    except Exception as e:
        print(e)

    print()


if __name__ == "__main__":
    summary('')
