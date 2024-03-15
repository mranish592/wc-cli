#! /bin/bash
wc_cli_alias_name=my-wc
workdir=$(pwd)

if ! grep -q "alias $wc_cli_alias_name=" ~/.zshrc; then
    echo "alias $wc_cli_alias_name='python3 ${workdir}/wc_cli.py'" >> ~/.zshrc
    source ~/.zshrc
    echo "Alias '$wc_cli_alias_name' added successfully."
else
    echo "Alias '$wc_cli_alias_name' already exists."
fi
