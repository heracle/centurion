
if [ $1 ]; then
  cp strategy_template.py $1.py
  echo "[+] Strategy created in $1.py"
else
  echo "[-] You must provide the name of the strategy"
  echo "[-] Example: ./new_strategy usa"
fi
