Title: Regex Cheat Sheet
Date: 2020-08-20


A [regular expression]((https://en.wikipedia.org/wiki/Regular_expression)) or pattern is used to go through a text and find a target string that meets the specified requirements. Most formalisms provide the following operations to construct regular expressions:

- __Boolean "or"__: A vertical bar separates alternatives. For example, `gray|grey` can match "gray" or "grey".  
- __Grouping__: Parentheses are used to define the scope and precedence of the operators (among other uses). For example, `gray|grey` and `gr(a|e)y` are equivalent. In the first case the options are 'gray' and 'grey', in the second the vowels 'a' and 'e' in the third position of the word.  
- __Quantification__: A quantifier after a token (such as a character) or group specifies how often that a preceding element is allowed to occur. The most common quantifiers are `?`, `*` and `+`. Other patterns are `{n}`, `{min,}`, `{,max}`, `{min,max}`, where `n` is the exact number of times.  
- __Wildcard__: The wildcard `.` matches any character.  

The pattern is composed of a sequence of atoms which try to match to the target string. The simplest atom is a literal, but grouping parts of the pattern to match an atom will require using `( )` as metacharacters. Metacharacters help form: 
- atoms; 
- quantifiers telling how many atoms (and whether it is a greedy quantifier or not); 
- a logical OR character, which offers a set of alternatives, and a logical NOT character, which negates an atom's existence; 
- and backreferences to refer to previous atoms of a completing pattern of atoms. 

Depending on the regex processor there are about fourteen metacharacters that may or may not have their literal character meaning, depending on context, or whether they are "escaped", i.e. preceded by an escape sequence, in this case, the backslash \. 
The usual metacharacters are `{}[]()^$.|*+?` and `\`. The usual characters that become metacharacters when escaped are `dswDSW` and `N`. 

When entering a regex in a programming language or text editor, they are usually quoted; this is common in C, Java, and Python for instance. However, they are often written with slashes as *delimiters*, as in `/re/` for the regex `re`. This originates in ed, where `/` is the editor command for searching, and an expression `/re/` can be used to specify a range of lines (matching the pattern), which can be combined with other commands on either side, most famously `g/re/p` as in `grep`. A similar convention is used in `sed`, where search and replace is given by `s/re/replacement/` and patterns can be joined with a comma to specify a range of lines as in `/re1/,/re2/`. 

__Character classes__: The character class is the most basic regex concept after a literal match. It makes one small sequence of characters match a larger set of characters. For example, [A-Z] could stand for the uppercase alphabet in the English language, and `\d` could mean any digit. 

When specifying a range of characters, such as `[a-Z]` the computer's locale settings determine the contents by the numeric ordering of the character encoding. 

A __replacement string__, also known as the replacement text, is the text that each regular expression match is replaced with during a search-and-replace. In most applications, the replacement text supports special syntax that allows you to reuse the text matched by the regular expression or parts thereof in the replacement. The simplest replacement text consists of only literal characters. You can use special character sequences to put non-printable characters in your regular expression.

Within the regular expression, you can use the __backreference__ `\1` to match the same text that was matched by the capturing group within `( )`. `([abc])=\1` matches `a=a`, `b=b`, and `c=c`. It does not match anything else. If your regex has multiple capturing groups, they are numbered counting their opening parentheses from left to right. If your regex has many groups, keeping track of their numbers can get cumbersome. Make your regexes easier to read by naming your groups. `(?<mygroup>[abc])=\k<mygroup>` is identical to `([abc])=\1`, except that you can refer to the group by its name.


*__Source__: [Wikipedia](https://en.wikipedia.org/wiki/Regular_expression) and [regular-expressions.info](https://www.regular-expressions.info/quickstart.html).*


## Regex Cheat Sheet

### Anchors
Anchors do not match any characters. They match a position.

|Symbol| Meaning                |
|:----:|:----------------------:|
| ^    | Start of a line        |
| \A   | Start of string        |
| $    | End of line            |
| \Z   | End of string          |
| \b   | Word boundary          |
| \B   | Not word boundary      |
| \<   | Start of word          |
| \>   | End of word            |



### Character Classes

|Symbol| Meaning                |
|:----:|:----------------------:|
| \c   | Control character      |
| \s   | White space            |
| \S   | Not white space        |
| \d   | Digit                  |
| \D   | Not digit              |
| \w   | Word                   |
| \W   | Not word               |
| \x   | Hexade­cimal digit      |
| \O   | Octal digit            |

### Quantifiers

|Symbol| Meaning |Symbol| Meaning |
|:----:|:-------:|:----:|:-------:|
| *	| 0 or more	| {3}	| Exactly 3| 
| +	| 1 or more	| {3,}	| 3 or more|
| ?	| 0 or 1	| {3,5}	|3, 4 or 5 |

*Add a `?` to a quantifier to make it ungreedy.*  
The repetition operators or quantifiers are greedy. They expand the match as far as they can. The regex `<.+>` matches `<EM>first</EM>` in `This is a <EM>first</EM> test`. Place a question mark after the quantifier to make it lazy. `<.+?>` matches `<EM>` in the above string.
A better solution is to use the dot sparingly. Use `<[^<>]+>` to quickly match an HTML tag without regard to attributes. The negated character class is more specific than the dot, which helps the regex engine find matches quickly.


### Groups and Ranges

|Symbol| Meaning                 |
|:-----:|:----------------------:|
| .     | Any character except new line (\n) |
| (a|b) | a or b |
| (...)	| Group |
|(?:...)| Passive (non-c­apt­uring) group |
| [abc]	| Range (a or b or c) |
| [^abc]| Not (a or b or c) |
| [a-q]	| Lower case letter from a to q |
| [A-Q]	| Upper case letter from A to Q |
| [0-7]	|Digit from 0 to 7 |
| \x    | Group/­sub­pattern number "­x" |

*Ranges are inclusive*.


### String Replacement

|Symbol| Meaning                 |
|:-----:|:----------------------:|
| $n	| nth non-pa­ssive group |
| $2 	| "­xyz­" in /^(abc­(xy­z))$/ |
| $1 	| "­xyz­" in /^(?:a­bc)­(xyz)$/|
| $\`    | Before matched string |
| $'	| After matched string |
| $+	| Last matched string |
| $&	| Entire matched string |

*Some regex implem­ent­ations use `\` instead of `$`.*

### Assertions
Lookahead and lookbehind, collectively called “lookaround”, are zero-length assertions just like the start and end of line, and start and end of word anchors. The difference is that lookarounds match characters, but then return *only* the result: match or no match. That is why they are called “assertions”. They do not consume characters in the string, but only assert whether a match is possible or not.

__Negative lookahead__ is indispensable to match something not followed by something else: e.g. `q(?!u)` to match a q not followed by a u. The negative lookahead construct is the pair of parentheses, with the opening parenthesis followed by a question mark and an exclamation point. Inside the lookahead, we have the trivial regex u.

__Positive lookahead__ works just the same. `q(?=u)` matches a q that is followed by a u, without making the u part of the match. The positive lookahead construct is a pair of parentheses, with the opening parenthesis followed by a question mark and an equals sign.

You can use any regular expression inside the lookahead (but not lookbehind). If it contains capturing groups then those groups will capture as normal and backreferences to them will work normally, even outside the lookahead. The lookahead itself is not a capturing group. It is not included in the count towards numbering the backreferences. If you want to store the match of the regex inside a lookahead, you have to put capturing parentheses around the regex inside the lookahead, like this: `(?=(regex))`. The other way around will not work, because the lookahead will already have discarded the regex match by the time the capturing group is to store its match.

__Lookbehind__ has the same effect, but works backwards. It tells the regex engine to temporarily step backwards in the string, and check if the text inside the lookbehind can be matched there. `(?<!a)b` matches a “b” that is not preceded by an “a”, using negative lookbehind. It doesn’t match *cab*, but matches the *b* (and only the *b*) in *bed* or *debt*. `(?<=a)b` (positive lookbehind) matches the *b* (and only the *b*) in *cab*, but does not match *bed* or *debt*.

The construct for positive lookbehind is `(?<=text)`. Negative lookbehind is written as `(?<!text)`.

You can use lookbehind anywhere in the regex, not only at the start. To find a word not ending with an “s”, you could use `\b\w+(?<!s)\b`, which is not the same as `\b\w+[^s]\b`. 

|Symbol| Meaning                 |
|:-----:|:----------------------:|
| `?=`	| Lookahead assertion |
| `?!`	| Negative lookahead |
| `?<=`	| Lookbehind assertion |
| `?!=` or `?<!` |	Negative lookbehind |
| `?>`	| Once-only subexp­ression |
| `?()`	| Condition [if then] |
| `?()|`| Condition [if then else]|
| `?#`	| Comment |

## Commonly Used Regex

New line: `[\r\n]|$`  
Line contains only whole number: `^\d+$`  
Line contains only 11-digit number: `^\d{11}$`  

Whole line containing a specific set of words: `^.*\bwords_to_find\b.*$`

Word tokenization: `[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+`

Sentence tokenization: `(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s` *(using re.split() in Python)*


### XML/HTML/CSS Tags
XML Tags: `<(?:[^"']+?|.+?(?:"|').*?(?:"|')?.*?)*?>`

Elements with Attributes: `<\/?[\w\s]*>|<.+[\W]>`

HTML Image Sources: `<\s*img[^>]+src\s*=\s*(["'])(.*?)\1[^>]*>`

Hex Color Values: `#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})`

YouTube Video ID:  
`https?:\/\/(?:youtu\.be\/|(?:[a-z]{2,3}\.)?youtube\.com\/watch(?:\?|#\!)v=)([\w-]{11}).*/gi`

CSS Comments:  
`\/\*[^*]*\*+([^\/*][^*]*\*+)*\/`

### Dates

Date (YYYY-MM-dd):  
`([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))`
 
Date (dd-mmm-YYYY or dd/mmm/YYYY or dd.mmm.YYYY):  
`(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})`

### Time

Time Format HH:MM 12-hour, optional leading 0:  
`(0?[1-9]|1[0-2]):[0-5][0-9]`  
Time Format HH:MM 12-hour, optional leading 0, (AM/PM):  
`((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))`  
Time Format HH:MM 24-hour with leading 0:  
`(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]`  
Time Format HH:MM 24-hour, optional leading 0:  
`([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]`  
Time Format HH:MM:SS 24-hour:  
`(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)`  


### Digits

Whole Numbers: `\d+`  
Decimal Numbers: `\d*\.\d+`  
Whole + Decimal Numbers: `\d*(\.\d+)?`  
Negative, Positive Whole + Decimal Numbers: `-?\d*(\.\d+)?`  
Whole + Decimal + Fractions:  
`[-]?[0-9]+[,.]?[0-9]*([\/][0-9]+[,.]?[0-9]*)*`

### Alphanumeric Characters

Alphanumeric without space: `[a-zA-Z0-9]*`  
Alphanumeric with space: `[a-zA-Z0-9 ]*`

### Email

Common email Ids: `([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*`  
Uncommon email ids: `([a-z0-9_\.\+-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})`  


### Username

Alphanumeric string that may include _ and – having a length of 3 to 16 characters:  
`[a-z0-9_-]{3,16}`


### Duplicates in a String
`(\b\w+\b)(?=.*\b\1\b)`

### Phone Numbers
International phone numbers – with optional country code/extension:  
`(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?`

### File Paths
File path with filename and extension:  
`((\/|\\|\/\/|https?:\\\\|https?:\/\/)[a-z0-9 _@\-^!#$%&+={}.\/\\\[\]]+)+\.[a-z]+`

File path with optional filename, extension:  
`(.+)/([^/]+)`

File name with extension having 3 chars:  
`[\w,\s-]+\.[A-Za-z]{3}`


### URLs
Including http(s)  
`https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#()?&//=]*)`  

http(s) optional  
(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)`


### IP Addresses

IPv4 address:   
`(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])`

IPv6 address::    
`(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))`


### US States
`(?:A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])*`

