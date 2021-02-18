# The LAAC superdataset

The LAAC superdataset contains all the datasets of infant day-long recordings maintained by the LAAC team. Before anything, you are advised to read our documentation [here](https://laac-lscp.github.io/ChildRecordsData/).

## How to install the dataset

### Setup

- Setup DataLad. See the instructions [here](https://laac-lscp.github.io/ChildRecordsData/REUSE.html#installing-datalad).
- Setup your SSH access to GitHub. See the instructions [here](https://laac-lscp.github.io/ChildRecordsData/REUSE.html#setting-up-your-ssh-access-to-github).
- Setup your SSH access to Oberon. See the instructions [here](https://laac-lscp.github.io/ChildRecordsData/REUSE.html#setting-up-your-ssh-access-to-oberon).

### Installation

In order to install the superdataset, run the following commands :

```
datalad install -r git@github.com:LAAC-LSCP/datasets.git
cd datasets
datalad run-procedure setup <oberon_alias>
```

Make sure to replace <oberon_alias> with whatever alias you use to ssh into Oberon. If you have followed [our instructions](https://laac-lscp.github.io/ChildRecordsData/REUSE.html#setting-up-your-ssh-access-to-oberon), it should be `foberon`.

### Hurray

You're good to go. You can now download as much data as you want. Examples:

 - Download all annotations:
 
```bash
 datalad get */annotations
```
 
  - Download standardized recordings from tsimane2017:
  
```bash
 datalad get tsimane2017-data/recordings/converted/standard
```


