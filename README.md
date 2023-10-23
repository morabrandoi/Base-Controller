# Bass-Controller

## Steps So Far

- In terminal, CD into the "nxbt" directory cloned from github.
- There, make sure vagrant is running or run `vagrant up`
- Run `vagrant ssh` to connect to the vm.
- use `sudo nxbt tui` to connect to new switch
  - use `sudo nxbt tui -r` to reconnect to previously connected switch
- When moving scripts to guest vm don't forget to run `chmod +x start_server.sh` on the first time
- If it is the first time setting up vagrant add the guest files as a service on startup using systemd and systemctl

## Tools

- nxbt
- Vagrant

## Mapping

- Left Bumper: E1
- Left Trigger: F1
- Right Trigger: G1
- Right Bumber: G#1

- Left Stick to Left: A#1
- Left Stick to Right: C2
- Left Stick Click: B1
- Left Stick to Up: E2
- Left Stick to Down: F#1

- Right Stick to Left: F#2
- Right Stick to Right: G#2
- Right Stick Click: G2
- Right Stick to Up: C3
- Right Stick to Down: D2

- X: G3
- Y: C#3
- A: D#3
- B: A2
