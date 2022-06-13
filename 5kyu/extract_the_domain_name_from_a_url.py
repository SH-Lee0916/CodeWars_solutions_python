'''
https://www.codewars.com/kata/514a024011ea4fb54200004b/
'''

def domain_name(url):
    return url.replace("http://", "").replace("https://", "").replace("www.", "").split(".")[0]


if __name__ == "__main__":
    print(domain_name("http://google.com"), "google")
    print(domain_name("http://google.co.jp"), "google")
    print(domain_name("www.xakep.ru"), "xakep")
    print(domain_name("https://youtube.com"), "youtube")