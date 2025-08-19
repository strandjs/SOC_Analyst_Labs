**Volatility** is the world's most widely used framework for extracting digital artifacts from volatile memory (RAM) samples. The extraction techniques are performed completely independent of the system being investigated but offer visibility into the runtime state of the system. The framework is intended to introduce people to the techniques and complexities associated with extracting digital artifacts from volatile memory samples and provide a platform for further work into this exciting area of research

[Volatility Main Github Repo](https://github.com/volatilityfoundation/volatility3)

Volatility 3 is a complete rewrite of the original framework released in 2019, built to address performance, architecture, and modularity limitations of Volatility 2. It features an improved license (Volatility Software License), clean design, and better extensibility

## Setup

All you need is to clone it's repo and cd in
```bash
git clone https://github.com/volatilityfoundation/volatility3.git 
```
```bash
cd volatility3
```

To run it do
```bash
python3 vol.py
```

## Usage

To list needed plugins and get help you can use

- For **Windows**
```bash
python3 vol.py -h | grep windows
```

- For **Linux**
```bash
python3 vol.py -h | grep linux
```

- For general help
```bash
python3 vol.py -h
```

- For specific commands ( change ``windows.pslist.PsList`` with whatever command you wish )
```bash
python3 vol.py windows.pslist.PsList -h
```
