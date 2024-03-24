#! /bin/bash
wc_cli_alias_name=wc-cli
workdir=$(pwd)

if ! grep -q "alias $wc_cli_alias_name=" ~/.bashrc; then
    echo "alias $wc_cli_alias_name='python3 ${workdir}/wc-cli/wc_cli.py'" >> ~/.bashrc
    source ~/.bashrc
    echo "Alias '$wc_cli_alias_name' added successfully."
else
    echo "Alias '$wc_cli_alias_name' already exists."
fi
