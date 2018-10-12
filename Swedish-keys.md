Add this to /usr/share/X11/xkb/symbols/us:
```bash
partial alphanumeric_keys
xkb_symbols "swedish" {

    include "us(basic)"
    name[Group1]= "English (US, with åäö)";

    key <AD11> { [ bracketleft,  braceleft,  aring,       Aring      ] };
    key <AC10> { [ semicolon,    colon,      odiaeresis,  Odiaeresis ] };
    key <AC11> { [ apostrophe,   quotedbl,   adiaeresis,  Adiaeresis ] };

    include "level3(ralt_switch)"
};

```

and this to /usr/share/X11/xkb/rules/evdev.xml:
Search for ```<name>us</name>```
```xml
<variant>
  <configItem>
    <name>swedish</name>
    <description>English (US, with åäö)</description>
  </configItem>
</variant>

```
That will let you access å, ä and ö via AltGr (RightAlt), which is the conventional way to access third and fourth level symbols.