from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):
    
    # G, H = utils.make_generators(num=2, seed=42)
    r1 = Secret(utils.get_random_num(bits=128))
    r2 = Secret(utils.get_random_num(bits=128))

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    n = utils.get_random_num(bits=128)
    m1, m2 = Secret(n), Secret(n)

    C1 = r1.value * G
    C2 = m1.value * G + r1.value * H

    D1 = r2.value * G
    D2 = m1.value * G + r2.value * H

    #Generate a NIZK proving equality of the plaintexts
    stmt = DLRep(C1, r1*G) & DLRep(C2, r1*H+m1*G) & DLRep(D1, r2*G) & DLRep(D2, r2*H+m1*G)
    
    zk_proof = stmt.prove() 

    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof

