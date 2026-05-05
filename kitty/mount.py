import sys

from kitty.boss import Boss, Window
from kittens.tui.handler import result_handler

def main(args: list[str]) -> str:
    stdin_data: str = sys.stdin.read()
    return stdin_data

def mount(stdin_data: str, w: Window, boss: Boss, ) -> None:
    disk_data: list[str] = stdin_data.strip().split()
    if len(disk_data) < 3:
        return
    
    device_path: str = "/dev/" + disk_data[0]
    fs: str = disk_data[1]
    mount_point: str = "/media/$USER/" + disk_data[2]

    for i in range(len(disk_data[2:]) - 1):
        mount_point += " " + disk_data[3 + i]
    
    boss.call_remote_control(w, ("send_text", "\x01\x0B"))
    boss.call_remote_control(w, ("send_text", 
                                 f"sudo mount \"{device_path}\" \"{mount_point}\" -t {fs}"))

@result_handler(type_of_input='selection')
def handle_result(args: list[str], stdin_data: str,
                  target_window_id: int, boss: Boss) -> None:
    if not stdin_data:
        return

    w: Window = boss.window_id_map.get(target_window_id)
    if w is None:
        return
    
    mount(stdin_data, w, boss)