#!/opt/splunk/bin/python

feed = [
    "Alienvault IP Reputation",
    "Bad IPs",
    "BBcan177 DNSBL",
    "BBcan177 Malicious IPs",
    "Blocklist.de Blocklist",
    "Botvrij.eu - domains",
    "Botvrij.eu - hostnames",
    "Botvrij.eu - ips",
    "Botvrij.eu - urls",
    "Brute Force Blocker",
    "C&C Domains",
    "C&C IPs",
    "CI Bad Guys",
    "CoinBlocker Domains",
    "Compromised IPs",
    "Cridex IPs",
    "Darklist",
    "Dictionary SSH Attacks",
    "Domains Blacklist",
    "Dyre Botnet IPs",
    "Feodo Tracker",
    "GreenSnow Blacklist",
    "Hancitor IPs",
    "High Confidence IPv4 Drop List",
    "Immortal Malware Domains",
    "IPSpamList",
    "Malicious EXE IPs",
    "Malicious EXE URLs",
    "Malware Corpus Tracker",
    "Malware Domains List",
    "Malware Domains",
    "Monero Miner",
    "NoCoin",
    "OpenPhish",
    "PhishTank",
    "Ransomware Domains",
    "Ransomware IPs",
    "Ransomware URLs",
    "Simple Malware List",
    "SSL BL",
    "Suspicious Domains",
    "Suspicious Dynamic DNS Providers",
    "Talos IP Blacklist",
    "TOR IPs",
    "URLhaus",
    "ZeroDot1's Bad IPs Feed",
    "Zeus Bad Domains",
    "Zeus Bad IPs"
]

threat = [
    "Addrop",
    "Adposhel",
    "Adware",
    "Adwind",
    "AFRF",
    "AgentTesla",
    "AKBuilder",
    "Android malware",
    "Android Trojan",
    "Androm",
    "Andromeda",
    "APT28",
    "Artemis",
    "Asparnet",
    "AutoHK",
    "AzorUlt Version 2",
    "AZORult",
    "Bad Rabbit",
    "Bamital",
    "Banjori",
    "Barys",
    "Bedep",
    "Beebone",
    "Bitcoin.Scammer",
    "BitCoinMiner",
    "Bitpaymer",
    "Bladabindi",
    "Bodegun",
    "CandyOpen",
    "Carberp",
    "Cduit",
    "Certutil",
    "Cobalt",
    "Coinhive",
    "CoinImp",
    "CoinMiner",
    "Comment Spam",
    "Conficker",
    "CozyDuke",
    "Crimson",
    "Cryptojacking",
    "CryptoLocker",
    "Csfrsys",
    "Cutwail",
    "CVE-2016-5426",
    "CVE-2017-11882",
    "CVE-2018-11776",
    "CyberGhost VPN",
    "DanaBot",
    "DarkKomet",
    "Dharma",
    "Dircrypt",
    "Domestic Kitten (Iranian Group)",
    "Dorifel",
    "Dreambot",
    "Dridex",
    "DynAmite",
    "Dyre",
    "Ekisoli",
    "EmoooDld",
    "Emotet",
    "Enigma",
    "Eorezo",
    "Evo",
    "Executable Code",
    "FAREIT",
    "FileProxy",
    "FileTour",
    "Fobber",
    "FormBook",
    "FTP",
    "Fuery",
    "Gafgyt",
    "GameOver Zeus",
    "GandCrab",
    "GlobeImposter",
    "Godzilla",
    "Gootkit",
    "Gozi",
    "Graftor",
    "Grandsoft",
    "Hancitor",
    "Hesperbot",
    "Hidden Cobra",
    "Hiddentear",
    "HPLOKI",
    "Hupigon",
    "iBryte",
    "IcedId",
    "IIS Attack",
    "IMAP",
    "IMAP3 Attack",
    "Invisimole",
    "Johnnie",
    "JS Crypto Miner",
    "Kardon Loader",
    "Kazy",
    "KillRabit",
    "Kovtar",
    "Kraken Botnet",
    "Krypt",
    "Kryptik",
    "Liusky",
    "Locky",
    "LokiBot",
    "Magecart",
    "MalDoc",
    "Malware",
    "Matsnu",
    "Mikey",
    "Mimikatz",
    "Mirai",
    "Monero",
    "MoneyTaker",
    "MS-DS Attack",
    "MS-SQL Attack",
    "MSIL",
    "Murofet",
    "MySQL Attack",
    "Nanobot",
    "NanoCore RAT",
    "Necurs",
    "Nemesis",
    "Nemucod",
    "Netbios Attack",
    "NetFilter",
    "NetSup",
    "Netwire",
    "Neutrino",
    "Nuclear Exploit Kit",
    "Nymaim",
    "OnionDuke",
    "Open Directory",
    "Operation Transparent Tribe",
    "OrcusRAT",
    "p2pgoz",
    "PandaZeuS",
    "Perseus",
    "Petya",
    "Philadelphia",
    "Phishing",
    "Pizd",
    "PlugX",
    "Pony",
    "POP Attack",
    "POPS Attack",
    "Postfix",
    "Predatorstealer",
    "Presenoker",
    "Proslikefan",
    "Proxy Scan",
    "PushIran.DL",
    "Pykspa",
    "Qadars",
    "qakbot",
    "Qealler",
    "qrat",
    "Quakbot",
    "QuantLoader",
    "Ramdo",
    "Ramnit",
    "Ranbyus",
    "Rapid",
    "Razy",
    "RDP Attack",
    "Rebhip",
    "Remcos RAT",
    "RemoteAdmin.RemoteUtilities.A",
    "RevCodeRAT",
    "RevengeRat",
    "RIG",
    "Rozena",
    "RPC-WIN Attack",
    "RpcBind Attack",
    "Ryuk",
    "Sality",
    "SamSam",
    "Sarvdap",
    "SASL_Brute_Force",
    "SASL_Bruteforce",
    "ServStart",
    "Shade",
    "Shellbot",
    "Shelma",
    "Shiotob",
    "Shylock",
    "Silence",
    "Simda",
    "SIP Attacks",
    "Smoke Loader",
    "SMTP Attack",
    "Socks Scan",
    "Sohanad",
    "Spamming",
    "Spear Phishing",
    "Sphinx",
    "Spursint",
    "SSH Brute Force",
    "StealthAgent",
    "Stratos",
    "Strictor",
    "Suppobox",
    "Swisyn",
    "Swrort",
    "Symmi",
    "SynAck",
    "Telnet",
    "tempedreve",
    "Themida",
    "Tiny Banker",
    "tofsee",
    "TOR Proxy",
    "TorJok",
    "Tovkater",
    "TrickBot",
    "TROJ_GEN.R020C0PF718",
    "Troj.Downloader.W32.Mediaget",
    "Trojan-Downloader.NSIS",
    "Trojan.BAT.Agent",
    "Trojan",
    "Unclassified",
    "unknowndropper",
    "unknownjs",
    "UrlMal",
    "Ursu",
    "Valyria",
    "Vawtrak",
    "Vigorf",
    "Virut",
    "VNC Attack",
    "volatile cedar / explosive",
    "VPNFilter",
    "Wannacry",
    "Web Hacking",
    "Win32:Dropper-FSB [Drp]",
    "Win32.Trojan.Agent",
    "Win32.Trojan.WisdomEyes",
    "X-Windows Attack",
    "XSSShell",
    "xTreme RAT",
    "ZapSpot",
    "Zeus",
    "Zoopark",
    "Zusy"
]