import sys
import logging

def afiseaza(ceva = 'salut'):
    for it, elem in enumerate(ceva):
        if it % 2 == 1:
            print elem

# logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
#                     level = logging.NOTSET)

# logging.info("Mesaj de informare")
# logging.warn("Mesaj de warning")
# logging.error("Mesaj de eroare")

def main():
    afiseaza(sys.argv[1])

if __name__ == '__main__':
    main()
