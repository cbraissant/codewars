'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''


'''
first solution
'''
def domain_name(url):
    if ('//') in url:
        url = url.split('//')[1]
    if ('www.') in url:
        url = url.split('www.')[1]
    return url.split('.')[0]


'''
using index [-1] to avoid the 'if' condition
'''
def domain_name(url):
    url = url.split('//')[-1]
    url = url.split('www.')[-1]
    return url.split('.')[0]


'''
same as a one-line
'''
def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


if __name__ == "__main__":
    import codewars_test as Test
    Test.assert_equals(domain_name("http://google.com"), "google")
    Test.assert_equals(domain_name("http://google.co.jp"), "google")
    Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
    Test.assert_equals(domain_name("https://youtube.com"), "youtube")