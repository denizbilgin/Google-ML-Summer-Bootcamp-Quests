'''
Buradaki görev bir çiçek tarlasının içerisinde bizim belirlediğimiz
bir kombinasyon var mı yok mu ona bakmak olacaktır.

Örnek:
Çiçek tarlamız şu şekilde olsun:
SITLMPPTRM
RSLFFPTRFV
TVTTIMIRML
LTLDPTVLIM
IIIVPDPTFL
PRLLTMPLSM
RMSLPLDIVL
SDPLFDRRDF
DTLMITIVPR
MRDSVIMFLS

Ve şimdi bu tarlada arayacağımız kombinasyon da şu olsun.
VPDP
LTMP
LPLD

Eğer bu kombinasyon aynen bu şekilde tarlada varsa "YES" yoksa da "NO" return eden bir fonksiyon yazmalısın.
'''

# Do not import any additional libraries
import math
import os
import random
import re
import sys

# Complete the 'flower_search' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING G
#  2. STRING P
def get_length_of_line(P):
    '''
    This function takes a string (as P) and counts how many flowers are next to each other (in a line)
    :param P: string
    :return: x
    '''
    splitted_P = P.split("\n")
    x = 0
    for i in range(len(splitted_P[0])):
        x += 1
    return x

def flower_search(G, P):
    # YOUR CODE HERE
    # Splitting the strings to loop easily
    splitted_G = G.split("\n")
    splitted_P = P.split("\n")
    x = get_length_of_line(P)

    # Some variables to keep necessary things
    start_index = 0
    end_index = 0
    index_of_P = 0

    # Looping rows
    for i in range(len(splitted_G)):

        # I take the elements of the specified splitted_G from start_index to end_index and check if they are in the splitted_P
        if splitted_G[i][start_index:end_index] == splitted_P[index_of_P]:

            # Is P in the Garden
            if index_of_P == len(splitted_P)-1:
                return "YES"
            else:
                # I'm increasing this variable because the research is not finished yet, other elements of splitted_P need to be searched as well
                index_of_P += 1
        else:

            # Looping columns
            for j in range(len(splitted_G[i]) - x + 1):

                # Define the start_index and end_index
                if (splitted_P[index_of_P] == splitted_G[i][j:j+x]):
                    start_index = j
                    end_index = j + x
                    index_of_P += 1
                    break
    return "NO"

if __name__ == '__main__':
    test_garden = "SITLMPPTRM\nRSLFFPTRFV\nTVTTIMIRML\nLTLDPTVLIM\nIIIVPDPTFL\nPRLLTMPLSM\nRMSLPLDIVL\nSDPLFDRRDF\nDTLMITIVPR\nMRDSVIMFLS"
    test_flower_1 = "VPDP\nLTMP\nLPLD"
    test_flower_2 = "VV\nVV"
    assert flower_search(test_garden, test_flower_1) == "YES"
    assert flower_search(test_garden, test_flower_2) == "NO"
    print("First test succeed")
    print("-------------------------------------")
    test_garden2 = "FILMPRSTVD\nDVTSRPMLIF\nFFFFFFFFFF\nFFFFFFFFFF\nIIIIIIIIII"
    test_flower_3 = "TSRPML\nFFFFFF\nFFFFFF"
    assert flower_search(test_garden2, test_flower_3) == "YES"
    print("Second test succeed")
