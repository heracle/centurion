
if [ $1 ]; then
  echo "----"
  echo $1
  cp strategy_template.py $1.py
  echo "[+] Strategy created in $1.py"
else
  echo "[-] You must provide the name of the strategy"
  echo "[-] Example: ./new_strategy usa"
fi