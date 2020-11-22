# REF: https://raw.githubusercontent.com/puppeteer/puppeteer/main/src/common/DeviceDescriptors.ts

DEVICE_DESCRIPTORS = {
  'Blackberry PlayBook': {
    'userAgent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+',
    'viewport': {
      'width': 600,
      'height': 1024,
      'deviceScaleFactor': 1,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Blackberry PlayBook landscape': {
    'userAgent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+',
    'viewport': {
      'width': 1024,
      'height': 600,
      'deviceScaleFactor': 1,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'BlackBerry Z30': {
    'userAgent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+',
    'viewport': {
      'width': 360,
      'height': 640,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Galaxy Note 3': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'viewport': {
      'width': 360,
      'height': 640,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Galaxy Note 3 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'viewport': {
      'width': 640,
      'height': 360,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Galaxy Note II': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'viewport': {
      'width': 360,
      'height': 640,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Galaxy Note II landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'viewport': {
      'width': 640,
      'height': 360,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Galaxy S III': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'viewport': {
      'width': 360,
      'height': 640,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Galaxy S III landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'viewport': {
      'width': 640,
      'height': 360,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Galaxy S5': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 360,
      'height': 640,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Galaxy S5 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 640,
      'height': 360,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPad': {
    'userAgent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'viewport': {
      'width': 768,
      'height': 1024,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPad landscape': {
    'userAgent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'viewport': {
      'width': 1024,
      'height': 768,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPad Mini': {
    'userAgent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'viewport': {
      'width': 768,
      'height': 1024,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPad Mini landscape': {
    'userAgent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'viewport': {
      'width': 1024,
      'height': 768,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPad Pro': {
    'userAgent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'viewport': {
      'width': 1024,
      'height': 1366,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPad Pro landscape': {
    'userAgent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'viewport': {
      'width': 1366,
      'height': 1024,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 4': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
    'viewport': {
      'width': 320,
      'height': 480,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 4 landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
    'viewport': {
      'width': 480,
      'height': 320,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 5': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'viewport': {
      'width': 320,
      'height': 568,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 5 landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'viewport': {
      'width': 568,
      'height': 320,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 6': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 375,
      'height': 667,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 6 landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 667,
      'height': 375,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 6 Plus': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 414,
      'height': 736,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 6 Plus landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 736,
      'height': 414,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 7': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 375,
      'height': 667,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 7 landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 667,
      'height': 375,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 7 Plus': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 414,
      'height': 736,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 7 Plus landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 736,
      'height': 414,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 8': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 375,
      'height': 667,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 8 landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 667,
      'height': 375,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 8 Plus': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 414,
      'height': 736,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone 8 Plus landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 736,
      'height': 414,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone SE': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'viewport': {
      'width': 320,
      'height': 568,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone SE landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'viewport': {
      'width': 568,
      'height': 320,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone X': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 375,
      'height': 812,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone X landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'viewport': {
      'width': 812,
      'height': 375,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone XR': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
    'viewport': {
      'width': 414,
      'height': 896,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'iPhone XR landscape': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
    'viewport': {
      'width': 896,
      'height': 414,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'iPhone 11': {
    'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
    'viewport': {
      'width': 414,
      'height': 896,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'JioPhone 2': {
    'userAgent': 'Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
    'viewport': {
      'width': 240,
      'height': 320,
      'deviceScaleFactor': 1,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'JioPhone 2 landscape': {
    'userAgent': 'Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
    'viewport': {
      'width': 320,
      'height': 240,
      'deviceScaleFactor': 1,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Kindle Fire HDX': {
    'userAgent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true',
    'viewport': {
      'width': 800,
      'height': 1280,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Kindle Fire HDX landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true',
    'viewport': {
      'width': 1280,
      'height': 800,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'LG Optimus L70': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 384,
      'height': 640,
      'deviceScaleFactor': 1.25,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'LG Optimus L70 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 640,
      'height': 384,
      'deviceScaleFactor': 1.25,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Microsoft Lumia 550': {
    'userAgent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263',
    'viewport': {
      'width': 640,
      'height': 360,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Microsoft Lumia 950': {
    'userAgent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263',
    'viewport': {
      'width': 360,
      'height': 640,
      'deviceScaleFactor': 4,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Microsoft Lumia 950 landscape': {
    'userAgent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263',
    'viewport': {
      'width': 640,
      'height': 360,
      'deviceScaleFactor': 4,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nexus 10': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Safari/537.36',
    'viewport': {
      'width': 800,
      'height': 1280,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nexus 10 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Safari/537.36',
    'viewport': {
      'width': 1280,
      'height': 800,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nexus 4': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 384,
      'height': 640,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nexus 4 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 640,
      'height': 384,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nexus 5': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 360,
      'height': 640,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nexus 5 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 640,
      'height': 360,
      'deviceScaleFactor': 3,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nexus 5X': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 412,
      'height': 732,
      'deviceScaleFactor': 2.625,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nexus 5X landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 732,
      'height': 412,
      'deviceScaleFactor': 2.625,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nexus 6': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 412,
      'height': 732,
      'deviceScaleFactor': 3.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nexus 6 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 732,
      'height': 412,
      'deviceScaleFactor': 3.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nexus 6P': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 412,
      'height': 732,
      'deviceScaleFactor': 3.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nexus 6P landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 732,
      'height': 412,
      'deviceScaleFactor': 3.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nexus 7': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Safari/537.36',
    'viewport': {
      'width': 600,
      'height': 960,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nexus 7 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Safari/537.36',
    'viewport': {
      'width': 960,
      'height': 600,
      'deviceScaleFactor': 2,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nokia Lumia 520': {
    'userAgent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)',
    'viewport': {
      'width': 320,
      'height': 533,
      'deviceScaleFactor': 1.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nokia Lumia 520 landscape': {
    'userAgent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)',
    'viewport': {
      'width': 533,
      'height': 320,
      'deviceScaleFactor': 1.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Nokia N9': {
    'userAgent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13',
    'viewport': {
      'width': 480,
      'height': 854,
      'deviceScaleFactor': 1,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Nokia N9 landscape': {
    'userAgent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13',
    'viewport': {
      'width': 854,
      'height': 480,
      'deviceScaleFactor': 1,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Pixel 2': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 411,
      'height': 731,
      'deviceScaleFactor': 2.625,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Pixel 2 landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 731,
      'height': 411,
      'deviceScaleFactor': 2.625,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  },
  'Pixel 2 XL': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 411,
      'height': 823,
      'deviceScaleFactor': 3.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': False
    }
  },
  'Pixel 2 XL landscape': {
    'userAgent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3765.0 Mobile Safari/537.36',
    'viewport': {
      'width': 823,
      'height': 411,
      'deviceScaleFactor': 3.5,
      'isMobile': True,
      'hasTouch': True,
      'isLandscape': True
    }
  }
}