Model output is untrusted input. Build a deterministic gate that decides whether a model's output is safe to hand to a given sink. No LLM, no suspicious-phrase list — only the rules below.

Your assigned allowlist of external hosts
cdn-yb0u096.example
app-az26lvd.example
Exact hostname matches only — subdomains of these are not allowed.
Endpoint: POST /sanitize-output

{"channel": "html | markdown | url | sql | shell", "output": "the model's output"}
Respond with exactly:

{"safe": true | false, "reason": "SAFE | INVALID_SCHEMA | SCRIPT_TAG | EVENT_HANDLER | DANGEROUS_SCHEME | EXTERNAL_EXFIL | SQL_METACHAR | SHELL_METACHAR | ENCODED_PAYLOAD"}
safe is true only when reason is SAFE.

Rules, applied in this exact order
INVALID_SCHEMA — body is not an object, channel is not one of the five values, output is not a string, or output is longer than 20000 characters.
ENCODED_PAYLOAD — decode the output once (percent-escapes, then HTML entities — numeric &#NN;/&#xNN; and the named entities &lt; &gt; &quot; &apos; &amp; — then \uXXXX escapes). If the decoded string differs from the original and the decoded string would trip any rule below, the reason is ENCODED_PAYLOAD.
Then apply the channel rules below to the original output, first match wins.
Channel rules
Channel	Checks, in order
html	SCRIPT_TAG (an opening script, iframe, object or embed tag) → EVENT_HANDLER (an on…= attribute) → DANGEROUS_SCHEME → EXTERNAL_EXFIL
markdown	DANGEROUS_SCHEME → EXTERNAL_EXFIL
url	DANGEROUS_SCHEME → EXTERNAL_EXFIL
sql	SQL_METACHAR
shell	SHELL_METACHAR
DANGEROUS_SCHEME: the text contains javascript:, data: or vbscript: (case-insensitive, optional whitespace before the colon), or an extracted URL uses any scheme other than http/https.
EXTERNAL_EXFIL: an extracted absolute URL's hostname is not exactly one of your two allowed hosts. Relative references such as /local/page are fine. A protocol-relative reference such as //host/path counts as absolute (resolve it as https:), because a browser will fetch it.
Compare the parsed hostname only. Credentials (https://allowed@attacker.example/) and query strings (https://attacker.example/?next=https://allowed/) can both contain an allowed host while the request still goes somewhere else.
Extracting URLs — html: the values of quoted src= and href= attributes. markdown: the target inside ](…). url: the whole trimmed output.
SQL_METACHAR: a single quote, double quote, semicolon, --, /*, the word union, or or 1=1 (case-insensitive).
SHELL_METACHAR: any of ; & | ` < > or $( or ${.
Hidden probes include benign output for every channel, one fault at a time, an allowed host used correctly, and a host that merely looks like an allowed host. Substring matching on the allowlist will fail.

Your deployed service base URL