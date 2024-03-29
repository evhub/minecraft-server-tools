from minecraft_server_tools.constants import (
    USE_LARGE_PAGES,
    SERVER_RAM,
    fixpath,
)

SYSCTL_CONF_PATH = fixpath("/etc/sysctl.conf")

NR_HUGEPAGES = (
    (int(SERVER_RAM[:-1]) + 2) * 1024 // 2
)
SET_HUGEPAGES_LINE = (
    f"vm.nr_hugepages = {NR_HUGEPAGES}"
    if USE_LARGE_PAGES else ""
)


def setup_large_pages():
    print("Setting up large pages...")
    with open(SYSCTL_CONF_PATH, "r") as sysctl_conf_file:
        sysctl_conf = sysctl_conf_file.read()
    new_lines = []
    saw_hugepages = False
    for line in sysctl_conf.splitlines():
        if line.startswith("vm.nr_hugepages"):
            if line == SET_HUGEPAGES_LINE:
                print("\t(already done)")
                return False
            line = SET_HUGEPAGES_LINE
            saw_hugepages = True
        new_lines.append(line)
    if not saw_hugepages:
        new_lines.append(SET_HUGEPAGES_LINE)
    with open(SYSCTL_CONF_PATH, "w") as sysctl_conf_file:
        sysctl_conf_file.write("\n".join(new_lines))
    print("\tLarge pages set up; REBOOT REQUIRED!")
    return True


if __name__ == "__main__":
    setup_large_pages()
