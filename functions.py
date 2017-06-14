import pandas, numpy, seaborn, logging, matplotlib
import matplotlib.pyplot as plt  

'''
downloaded_predictor = mhcflurry.Class1AffinityPredictor.load()
#print "Supported Alleles":
#print(downloaded_predictor.supported_alleles)
#print(downloaded_predictor.predict(allele="HLA-A0201", peptides=["SIINFEKL", "SIINFEQL"]))
#print(downloaded_predictor.predict_to_dataframe(allele="HLA-A0201", peptides=["SIINFEKL", "SIINFEQL"]))
def prediction_using_peptide():
    return
def prediction_using_fatsa():
    return
'''



from mhcflurry import Class1AffinityPredictor
from mhctools import MHCflurry
from Bio import SeqIO


try:
    from StringIO import StringIO # Python 2
except ImportError:
    from io import StringIO # Python 3


DEFAULT_ALLELE = "HLA-A*02:01"

protein_sequence_list = ["ILYQVPFSV"]

def predict_peptide(protein_sequence_list=["ILYQVPFSVILYQVPFSV"]):
    predictor = MHCflurry(alleles=[DEFAULT_ALLELE])
    binding_predictions = predictor.predict_subsequences(protein_sequence_list,
        peptide_lengths=[9])
    
    prediction_scores = {
        (x.peptide, x.allele): x.affinity for x in binding_predictions
    }
    print(prediction_scores)
    return prediction_scores


fasta_example = '''>seq0\n
FQTWEEFSRAAEKLYLADPMKVRVVLKYRHVDGNLCIKVTDDLVCLVYRTDQAQDVKKIEKF\n
>seq1\n
KYRTWEEFTRAAEKLYQADPMKVRVVLKYRHCDGNLCIKVTDDVVCLLYRTDQAQDVKKIEKFHSQLMRLME LKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM\n
>seq2\n
EEYQTWEEFARAAEKLYLTDPMKVRVVLKYRHCDGNLCMKVTDDAVCLQYKTDQAQDVKKVEKLHGK'''

def predict_fasta(fasta_contents=fasta_example):
    protein_sequences = {
        record.id: str(record.seq) for record in
        SeqIO.parse(StringIO(fasta_example), "fasta")
    }
    print(predict_peptide(protein_sequences))

#predict_fasta()
#predict_peptide()


x = {('AHKGFKGVD', 'HLA-A*02:03'): 33732.113, ('AHYGSLPQK', 'HLA-A*02:03'): 29232.244, ('APKNMYKDS', 'HLA-A*02:03'): 29282.021, ('AQGTLSKIF', 'HLA-A*02:03'): 21871.734, ('ARHGFLPRH', 'HLA-A*02:03'): 29522.211, ('ARRELVISL', 'HLA-A*02:03'): 8050.3984, ('ARTAHYGSL', 'HLA-A*02:03'): 6369.3613, ('ASQKRPSQR', 'HLA-A*02:03'): 29561.625, ('ASTMDHARH', 'HLA-A*02:03'): 27637.232, ('ASTPGHTII', 'HLA-A*02:03'): 9344.3809, ('ATASTMDHA', 'HLA-A*02:03'): 774.39124, ('AVCLHNDRT', 'HLA-A*02:03'): 13653.803, ('CLHNDRTTI', 'HLA-A*02:03'): 54.82444, ('DAQGTLSKI', 'HLA-A*02:03'): 6287.0444, ('DENPVVHFF', 'HLA-A*02:03'): 26353.053, ('DHARHGFLP', 'HLA-A*02:03'): 27429.221, ('DRGAPKNMY', 'HLA-A*02:03'): 37072.965, ('DSHHPARTA', 'HLA-A*02:03'): 13919.927, ('DSIGRFFGG', 'HLA-A*02:03'): 21489.811, ('DSRSGSPMA', 'HLA-A*02:03'): 22468.354, ('DTGILDSIG', 'HLA-A*02:03'): 22949.926, ('EAVCLHNDR', 'HLA-A*02:03'): 26572.639, ('ELVISLIVE', 'HLA-A*02:03'): 13127.103, ('ENPVVHFFK', 'HLA-A*02:03'): 31164.961, ('FFGGDRGAP', 'HLA-A*02:03'): 27797.631, ('FFKNIVTPR', 'HLA-A*02:03'): 16769.977, ('FGGDRGAPK', 'HLA-A*02:03'): 32115.17, ('FKGVDAQGT', 'HLA-A*02:03'): 25585.334, ('FKLGGRDSR', 'HLA-A*02:03'): 32599.73, ('FKNIVTPRT', 'HLA-A*02:03'): 20089.936, ('FLPRHRDTG', 'HLA-A*02:03'): 438.6221, ('GAPKNMYKD', 'HLA-A*02:03'): 25972.857, ('GDRGAPKNM', 'HLA-A*02:03'): 26295.889, ('GFKGVDAQG', 'HLA-A*02:03'): 25392.596, ('GFLPRHRDT', 'HLA-A*02:03'): 25012.988, ('GGDRGAPKN', 'HLA-A*02:03'): 34359.062, ('GGRDSRSGS', 'HLA-A*02:03'): 27378.207, ('GHTIIYEAV', 'HLA-A*02:03'): 3867.0942, ('GILDSIGRF', 'HLA-A*02:03'): 9808.1172, ('GKGRKSAHK', 'HLA-A*02:03'): 35621.012, ('GRDSRSGSP', 'HLA-A*02:03'): 30652.928, ('GRFFGGDRG', 'HLA-A*02:03'): 28765.211, ('GRKSAHKGF', 'HLA-A*02:03'): 33188.883, ('GRTQDENPV', 'HLA-A*02:03'): 19883.338, ('GSKYLATAS', 'HLA-A*02:03'): 12438.368, ('GSLPQKSHG', 'HLA-A*02:03'): 22760.146, ('GSPMARREL', 'HLA-A*02:03'): 21473.441, ('GTLSKIFKL', 'HLA-A*02:03'): 2387.8921, ('GVDAQGTLS', 'HLA-A*02:03'): 21145.668, ('HARHGFLPR', 'HLA-A*02:03'): 26744.527, ('HFFKNIVTP', 'HLA-A*02:03'): 11107.992, ('HGFLPRHRD', 'HLA-A*02:03'): 29237.402, ('HGRTQDENP', 'HLA-A*02:03'): 35789.293, ('HGSKYLATA', 'HLA-A*02:03'): 2454.5938, ('HHPARTAHY', 'HLA-A*02:03'): 33089.332, ('HKGFKGVDA', 'HLA-A*02:03'): 24596.072, ('HPARTAHYG', 'HLA-A*02:03'): 22144.287, ('HRDTGILDS', 'HLA-A*02:03'): 22953.23, ('HTIIYEAVC', 'HLA-A*02:03'): 16978.891, ('HYGSLPQKS', 'HLA-A*02:03'): 27071.631, ('IFKLGGRDS', 'HLA-A*02:03'): 26090.955, ('IGRFFGGDR', 'HLA-A*02:03'): 28128.385, ('IIYEAVCLH', 'HLA-A*02:03'): 3129.1428, ('ILDSIGRFF', 'HLA-A*02:03'): 12741.486, ('IVTPRTPPP', 'HLA-A*02:03'): 17552.391, ('IYEAVCLHN', 'HLA-A*02:03'): 29652.543, ('KDSHHPART', 'HLA-A*02:03'): 12309.999, ('KGFKGVDAQ', 'HLA-A*02:03'): 28058.994, ('KGRKSAHKG', 'HLA-A*02:03'): 26839.217, ('KGVDAQGTL', 'HLA-A*02:03'): 15495.678, ('KIFKLGGRD', 'HLA-A*02:03'): 11047.162, ('KLGGRDSRS', 'HLA-A*02:03'): 5264.2607, ('KNIVTPRTP', 'HLA-A*02:03'): 21758.85, ('KNMYKDSHH', 'HLA-A*02:03'): 27891.342, ('KRPSQRHGS', 'HLA-A*02:03'): 30799.264, ('KSAHKGFKG', 'HLA-A*02:03'): 21826.664, ('KSHGRTQDE', 'HLA-A*02:03'): 29632.953, ('KYLATASTM', 'HLA-A*02:03'): 14942.691, ('LATASTMDH', 'HLA-A*02:03'): 26620.096, ('LDSIGRFFG', 'HLA-A*02:03'): 24512.17, ('LGGRDSRSG', 'HLA-A*02:03'): 29597.734, ('LHNDRTTIP', 'HLA-A*02:03'): 29659.729, ('LPQKSHGRT', 'HLA-A*02:03'): 27340.635, ('LPRHRDTGI', 'HLA-A*02:03'): 21194.648, ('LSKIFKLGG', 'HLA-A*02:03'): 17906.672, ('LVISLIVES', 'HLA-A*02:03'): 2312.6328, ('MARRELVIS', 'HLA-A*02:03'): 14322.633, ('MDHARHGFL', 'HLA-A*02:03'): 13630.904, ('MYKDSHHPA', 'HLA-A*02:03'): 12313.674, ('NIVTPRTPP', 'HLA-A*02:03'): 18200.408, ('NMYKDSHHP', 'HLA-A*02:03'): 2221.7256, ('NPVVHFFKN', 'HLA-A*02:03'): 26464.826, ('PARTAHYGS', 'HLA-A*02:03'): 28145.451, ('PGHTIIYEA', 'HLA-A*02:03'): 6550.8477, ('PKNMYKDSH', 'HLA-A*02:03'): 32447.842, ('PMARRELVI', 'HLA-A*02:03'): 9843.9795, ('PPPSQGKGR', 'HLA-A*02:03'): 35128.238, ('PPSQGKGRK', 'HLA-A*02:03'): 36721.508, ('PQKSHGRTQ', 'HLA-A*02:03'): 25875.324, ('PRHRDTGIL', 'HLA-A*02:03'): 17319.961, ('PRTPPPSQG', 'HLA-A*02:03'): 28054.926, ('PSQGKGRKS', 'HLA-A*02:03'): 31660.961, ('PSQRHGSKY', 'HLA-A*02:03'): 29938.455, ('PVVHFFKNI', 'HLA-A*02:03'): 7078.6846, ('QDENPVVHF', 'HLA-A*02:03'): 29692.33, ('QGKGRKSAH', 'HLA-A*02:03'): 35450.613, ('QGTLSKIFK', 'HLA-A*02:03'): 32298.014, ('QKRPSQRHG', 'HLA-A*02:03'): 31424.822, ('QKSHGRTQD', 'HLA-A*02:03'): 31810.807, ('QRHGSKYLA', 'HLA-A*02:03'): 23557.145, ('RDSRSGSPM', 'HLA-A*02:03'): 19732.35, ('RDTGILDSI', 'HLA-A*02:03'): 8146.9409, ('RELVISLIV', 'HLA-A*02:03'): 6302.6167, ('RFFGGDRGA', 'HLA-A*02:03'): 18407.014, ('RGAPKNMYK', 'HLA-A*02:03'): 36280.887, ('RHGFLPRHR', 'HLA-A*02:03'): 27742.043, ('RHGSKYLAT', 'HLA-A*02:03'): 18549.666, ('RHRDTGILD', 'HLA-A*02:03'): 30638.197, ('RKSAHKGFK', 'HLA-A*02:03'): 29711.508, ('RPSQRHGSK', 'HLA-A*02:03'): 35809.23, ('RRELVISLI', 'HLA-A*02:03'): 4515.1406, ('RSGSPMARR', 'HLA-A*02:03'): 28974.402, ('RTAHYGSLP', 'HLA-A*02:03'): 8029.8643, ('RTPPPSQGK', 'HLA-A*02:03'): 31925.109, ('RTQDENPVV', 'HLA-A*02:03'): 3474.1025, ('SAHKGFKGV', 'HLA-A*02:03'): 1402.7242, ('SGSPMARRE', 'HLA-A*02:03'): 31064.725, ('SHGRTQDEN', 'HLA-A*02:03'): 33669.41, ('SHHPARTAH', 'HLA-A*02:03'): 34270.344, ('SIGRFFGGD', 'HLA-A*02:03'): 17565.451, ('SKIFKLGGR', 'HLA-A*02:03'): 22575.059, ('SKYLATAST', 'HLA-A*02:03'): 5922.0986, ('SLPQKSHGR', 'HLA-A*02:03'): 13353.23, ('SPMARRELV', 'HLA-A*02:03'): 15914.104, ('SQGKGRKSA', 'HLA-A*02:03'): 8578.8691, ('SQKRPSQRH', 'HLA-A*02:03'): 25940.355, ('SQRHGSKYL', 'HLA-A*02:03'): 761.00885, ('SRSGSPMAR', 'HLA-A*02:03'): 30367.982, ('STMDHARHG', 'HLA-A*02:03'): 1211.0455, ('STPGHTIIY', 'HLA-A*02:03'): 23902.23, ('TAHYGSLPQ', 'HLA-A*02:03'): 23046.451, ('TASTMDHAR', 'HLA-A*02:03'): 25066.289, ('TGILDSIGR', 'HLA-A*02:03'): 27304.52, ('TIIYEAVCL', 'HLA-A*02:03'): 4642.0801, ('TLSKIFKLG', 'HLA-A*02:03'): 2667.3245, ('TMDHARHGF', 'HLA-A*02:03'): 17867.693, ('TPGHTIIYE', 'HLA-A*02:03'): 28877.355, ('TPPPSQGKG', 'HLA-A*02:03'): 32001.346, ('TPRTPPPSQ', 'HLA-A*02:03'): 33452.219, ('TQDENPVVH', 'HLA-A*02:03'): 25350.059, ('VCLHNDRTT', 'HLA-A*02:03'): 20978.83, ('VDAQGTLSK', 'HLA-A*02:03'): 34834.531, ('VHFFKNIVT', 'HLA-A*02:03'): 28177.357, ('VTPRTPPPS', 'HLA-A*02:03'): 18764.225, ('VVHFFKNIV', 'HLA-A*02:03'): 3361.6582, ('YEAVCLHND', 'HLA-A*02:03'): 29406.357, ('YGSLPQKSH', 'HLA-A*02:03'): 28645.225, ('YKDSHHPAR', 'HLA-A*02:03'): 30060.246, ('YLATASTMD', 'HLA-A*02:03'): 688.97162, ('AHKGFKGVD', 'HLA-A*02:01'): 23965.752, ('AHYGSLPQK', 'HLA-A*02:01'): 28604.305, ('APKNMYKDS', 'HLA-A*02:01'): 27835.434, ('AQGTLSKIF', 'HLA-A*02:01'): 21999.908, ('ARHGFLPRH', 'HLA-A*02:01'): 21607.668, ('ARRELVISL', 'HLA-A*02:01'): 6539.5371, ('ARTAHYGSL', 'HLA-A*02:01'): 20612.695, ('ASQKRPSQR', 'HLA-A*02:01'): 25613.945, ('ASTMDHARH', 'HLA-A*02:01'): 22988.742, ('ASTPGHTII', 'HLA-A*02:01'): 20675.795, ('ATASTMDHA', 'HLA-A*02:01'): 8404.5186, ('AVCLHNDRT', 'HLA-A*02:01'): 13737.524, ('CLHNDRTTI', 'HLA-A*02:01'): 3630.1321, ('DAQGTLSKI', 'HLA-A*02:01'): 16516.645, ('DENPVVHFF', 'HLA-A*02:01'): 20967.189, ('DHARHGFLP', 'HLA-A*02:01'): 26679.871, ('DRGAPKNMY', 'HLA-A*02:01'): 33920.672, ('DSHHPARTA', 'HLA-A*02:01'): 25523.043, ('DSIGRFFGG', 'HLA-A*02:01'): 13916.263, ('DSRSGSPMA', 'HLA-A*02:01'): 17349.42, ('DTGILDSIG', 'HLA-A*02:01'): 26079.062, ('EAVCLHNDR', 'HLA-A*02:01'): 25738.363, ('ELVISLIVE', 'HLA-A*02:01'): 10618.371, ('ENPVVHFFK', 'HLA-A*02:01'): 26982.861, ('FFGGDRGAP', 'HLA-A*02:01'): 22797.945, ('FFKNIVTPR', 'HLA-A*02:01'): 17019.273, ('FGGDRGAPK', 'HLA-A*02:01'): 30025.693, ('FKGVDAQGT', 'HLA-A*02:01'): 24890.939, ('FKLGGRDSR', 'HLA-A*02:01'): 21825.02, ('FKNIVTPRT', 'HLA-A*02:01'): 15112.604, ('FLPRHRDTG', 'HLA-A*02:01'): 5489.5806, ('GAPKNMYKD', 'HLA-A*02:01'): 28227.895, ('GDRGAPKNM', 'HLA-A*02:01'): 28056.479, ('GFKGVDAQG', 'HLA-A*02:01'): 25567.967, ('GFLPRHRDT', 'HLA-A*02:01'): 19689.059, ('GGDRGAPKN', 'HLA-A*02:01'): 29567.264, ('GGRDSRSGS', 'HLA-A*02:01'): 31422.725, ('GHTIIYEAV', 'HLA-A*02:01'): 7931.1157, ('GILDSIGRF', 'HLA-A*02:01'): 5453.7319, ('GKGRKSAHK', 'HLA-A*02:01'): 32603.09, ('GRDSRSGSP', 'HLA-A*02:01'): 31824.674, ('GRFFGGDRG', 'HLA-A*02:01'): 28704.676, ('GRKSAHKGF', 'HLA-A*02:01'): 30784.729, ('GRTQDENPV', 'HLA-A*02:01'): 17131.014, ('GSKYLATAS', 'HLA-A*02:01'): 20182.131, ('GSLPQKSHG', 'HLA-A*02:01'): 15177.396, ('GSPMARREL', 'HLA-A*02:01'): 21226.588, ('GTLSKIFKL', 'HLA-A*02:01'): 927.9411, ('GVDAQGTLS', 'HLA-A*02:01'): 18748.572, ('HARHGFLPR', 'HLA-A*02:01'): 27831.398, ('HFFKNIVTP', 'HLA-A*02:01'): 13283.956, ('HGFLPRHRD', 'HLA-A*02:01'): 24470.455, ('HGRTQDENP', 'HLA-A*02:01'): 32051.039, ('HGSKYLATA', 'HLA-A*02:01'): 5272.9683, ('HHPARTAHY', 'HLA-A*02:01'): 32031.635, ('HKGFKGVDA', 'HLA-A*02:01'): 28977.164, ('HPARTAHYG', 'HLA-A*02:01'): 27467.648, ('HRDTGILDS', 'HLA-A*02:01'): 24122.641, ('HTIIYEAVC', 'HLA-A*02:01'): 7228.1772, ('HYGSLPQKS', 'HLA-A*02:01'): 24584.252, ('IFKLGGRDS', 'HLA-A*02:01'): 26919.658, ('IGRFFGGDR', 'HLA-A*02:01'): 21002.393, ('IIYEAVCLH', 'HLA-A*02:01'): 4753.0156, ('ILDSIGRFF', 'HLA-A*02:01'): 3335.8826, ('IVTPRTPPP', 'HLA-A*02:01'): 20083.787, ('IYEAVCLHN', 'HLA-A*02:01'): 25797.34, ('KDSHHPART', 'HLA-A*02:01'): 23844.174, ('KGFKGVDAQ', 'HLA-A*02:01'): 22396.109, ('KGRKSAHKG', 'HLA-A*02:01'): 30194.625, ('KGVDAQGTL', 'HLA-A*02:01'): 17322.373, ('KIFKLGGRD', 'HLA-A*02:01'): 9293.2979, ('KLGGRDSRS', 'HLA-A*02:01'): 8121.187, ('KNIVTPRTP', 'HLA-A*02:01'): 20195.568, ('KNMYKDSHH', 'HLA-A*02:01'): 22592.332, ('KRPSQRHGS', 'HLA-A*02:01'): 31708.492, ('KSAHKGFKG', 'HLA-A*02:01'): 20105.461, ('KSHGRTQDE', 'HLA-A*02:01'): 23703.943, ('KYLATASTM', 'HLA-A*02:01'): 16573.242, ('LATASTMDH', 'HLA-A*02:01'): 23339.785, ('LDSIGRFFG', 'HLA-A*02:01'): 27160.977, ('LGGRDSRSG', 'HLA-A*02:01'): 30401.189, ('LHNDRTTIP', 'HLA-A*02:01'): 31583.125, ('LPQKSHGRT', 'HLA-A*02:01'): 33570.785, ('LPRHRDTGI', 'HLA-A*02:01'): 26493.588, ('LSKIFKLGG', 'HLA-A*02:01'): 14356.15, ('LVISLIVES', 'HLA-A*02:01'): 1933.124, ('MARRELVIS', 'HLA-A*02:01'): 15952.595, ('MDHARHGFL', 'HLA-A*02:01'): 22836.332, ('MYKDSHHPA', 'HLA-A*02:01'): 21456.104, ('NIVTPRTPP', 'HLA-A*02:01'): 26679.592, ('NMYKDSHHP', 'HLA-A*02:01'): 8022.1797, ('NPVVHFFKN', 'HLA-A*02:01'): 25964.66, ('PARTAHYGS', 'HLA-A*02:01'): 26375.934, ('PGHTIIYEA', 'HLA-A*02:01'): 4533.6382, ('PKNMYKDSH', 'HLA-A*02:01'): 25091.043, ('PMARRELVI', 'HLA-A*02:01'): 17878.176, ('PPPSQGKGR', 'HLA-A*02:01'): 33315.668, ('PPSQGKGRK', 'HLA-A*02:01'): 34280.543, ('PQKSHGRTQ', 'HLA-A*02:01'): 30879.379, ('PRHRDTGIL', 'HLA-A*02:01'): 23083.494, ('PRTPPPSQG', 'HLA-A*02:01'): 33819.02, ('PSQGKGRKS', 'HLA-A*02:01'): 31257.234, ('PSQRHGSKY', 'HLA-A*02:01'): 30690.018, ('PVVHFFKNI', 'HLA-A*02:01'): 11963.676, ('QDENPVVHF', 'HLA-A*02:01'): 28914.475, ('QGKGRKSAH', 'HLA-A*02:01'): 32752.051, ('QGTLSKIFK', 'HLA-A*02:01'): 29972.451, ('QKRPSQRHG', 'HLA-A*02:01'): 30982.504, ('QKSHGRTQD', 'HLA-A*02:01'): 32559.65, ('QRHGSKYLA', 'HLA-A*02:01'): 19795.963, ('RDSRSGSPM', 'HLA-A*02:01'): 28434.262, ('RDTGILDSI', 'HLA-A*02:01'): 8399.374, ('RELVISLIV', 'HLA-A*02:01'): 5603.6855, ('RFFGGDRGA', 'HLA-A*02:01'): 15219.808, ('RGAPKNMYK', 'HLA-A*02:01'): 30848.943, ('RHGFLPRHR', 'HLA-A*02:01'): 26999.541, ('RHGSKYLAT', 'HLA-A*02:01'): 26609.207, ('RHRDTGILD', 'HLA-A*02:01'): 30681.822, ('RKSAHKGFK', 'HLA-A*02:01'): 29363.734, ('RPSQRHGSK', 'HLA-A*02:01'): 34179.77, ('RRELVISLI', 'HLA-A*02:01'): 7008.1353, ('RSGSPMARR', 'HLA-A*02:01'): 27911.191, ('RTAHYGSLP', 'HLA-A*02:01'): 18083.916, ('RTPPPSQGK', 'HLA-A*02:01'): 31536.986, ('RTQDENPVV', 'HLA-A*02:01'): 2042.1199, ('SAHKGFKGV', 'HLA-A*02:01'): 12102.287, ('SGSPMARRE', 'HLA-A*02:01'): 26452.184, ('SHGRTQDEN', 'HLA-A*02:01'): 29724.488, ('SHHPARTAH', 'HLA-A*02:01'): 32207.184, ('SIGRFFGGD', 'HLA-A*02:01'): 17180.932, ('SKIFKLGGR', 'HLA-A*02:01'): 22335.684, ('SKYLATAST', 'HLA-A*02:01'): 11514.245, ('SLPQKSHGR', 'HLA-A*02:01'): 16480.596, ('SPMARRELV', 'HLA-A*02:01'): 17647.559, ('SQGKGRKSA', 'HLA-A*02:01'): 26044.168, ('SQKRPSQRH', 'HLA-A*02:01'): 32724.732, ('SQRHGSKYL', 'HLA-A*02:01'): 17843.854, ('SRSGSPMAR', 'HLA-A*02:01'): 32872.117, ('STMDHARHG', 'HLA-A*02:01'): 7421.9219, ('STPGHTIIY', 'HLA-A*02:01'): 25524.674, ('TAHYGSLPQ', 'HLA-A*02:01'): 25257.924, ('TASTMDHAR', 'HLA-A*02:01'): 26605.578, ('TGILDSIGR', 'HLA-A*02:01'): 20346.629, ('TIIYEAVCL', 'HLA-A*02:01'): 1609.134, ('TLSKIFKLG', 'HLA-A*02:01'): 4993.2271, ('TMDHARHGF', 'HLA-A*02:01'): 8239.8389, ('TPGHTIIYE', 'HLA-A*02:01'): 28306.584, ('TPPPSQGKG', 'HLA-A*02:01'): 31733.904, ('TPRTPPPSQ', 'HLA-A*02:01'): 34344.125, ('TQDENPVVH', 'HLA-A*02:01'): 20313.824, ('VCLHNDRTT', 'HLA-A*02:01'): 11237.161, ('VDAQGTLSK', 'HLA-A*02:01'): 30938.244, ('VHFFKNIVT', 'HLA-A*02:01'): 20447.312, ('VTPRTPPPS', 'HLA-A*02:01'): 17258.525, ('VVHFFKNIV', 'HLA-A*02:01'): 4231.2031, ('YEAVCLHND', 'HLA-A*02:01'): 24002.418, ('YGSLPQKSH', 'HLA-A*02:01'): 26976.48, ('YKDSHHPAR', 'HLA-A*02:01'): 28235.002, ('YLATASTMD', 'HLA-A*02:01'): 2392.0186, ('AHKGFKGVD', 'HLA-A*01:01'): 31529.709, ('AHYGSLPQK', 'HLA-A*01:01'): 31431.506, ('APKNMYKDS', 'HLA-A*01:01'): 33515.508, ('AQGTLSKIF', 'HLA-A*01:01'): 30608.672, ('ARHGFLPRH', 'HLA-A*01:01'): 30707.289, ('ARRELVISL', 'HLA-A*01:01'): 29673.025, ('ARTAHYGSL', 'HLA-A*01:01'): 35256.312, ('ASQKRPSQR', 'HLA-A*01:01'): 27955.199, ('ASTMDHARH', 'HLA-A*01:01'): 24735.635, ('ASTPGHTII', 'HLA-A*01:01'): 29922.785, ('ATASTMDHA', 'HLA-A*01:01'): 3276.8093, ('AVCLHNDRT', 'HLA-A*01:01'): 34207.098, ('CLHNDRTTI', 'HLA-A*01:01'): 32702.801, ('DAQGTLSKI', 'HLA-A*01:01'): 31058.918, ('DENPVVHFF', 'HLA-A*01:01'): 18942.26, ('DHARHGFLP', 'HLA-A*01:01'): 32567.383, ('DRGAPKNMY', 'HLA-A*01:01'): 27152.043, ('DSHHPARTA', 'HLA-A*01:01'): 33303.977, ('DSIGRFFGG', 'HLA-A*01:01'): 29756.51, ('DSRSGSPMA', 'HLA-A*01:01'): 27960.398, ('DTGILDSIG', 'HLA-A*01:01'): 26604.613, ('EAVCLHNDR', 'HLA-A*01:01'): 30927.801, ('ELVISLIVE', 'HLA-A*01:01'): 31433.215, ('ENPVVHFFK', 'HLA-A*01:01'): 25600.93, ('FFGGDRGAP', 'HLA-A*01:01'): 33963.656, ('FFKNIVTPR', 'HLA-A*01:01'): 32998.164, ('FGGDRGAPK', 'HLA-A*01:01'): 25208.158, ('FKGVDAQGT', 'HLA-A*01:01'): 33190.848, ('FKLGGRDSR', 'HLA-A*01:01'): 34149.176, ('FKNIVTPRT', 'HLA-A*01:01'): 31574.361, ('FLPRHRDTG', 'HLA-A*01:01'): 35173.898, ('GAPKNMYKD', 'HLA-A*01:01'): 29473.488, ('GDRGAPKNM', 'HLA-A*01:01'): 33628.145, ('GFKGVDAQG', 'HLA-A*01:01'): 32679.822, ('GFLPRHRDT', 'HLA-A*01:01'): 32864.0, ('GGDRGAPKN', 'HLA-A*01:01'): 30708.314, ('GGRDSRSGS', 'HLA-A*01:01'): 31552.117, ('GHTIIYEAV', 'HLA-A*01:01'): 29776.381, ('GILDSIGRF', 'HLA-A*01:01'): 27758.424, ('GKGRKSAHK', 'HLA-A*01:01'): 33255.578, ('GRDSRSGSP', 'HLA-A*01:01'): 29808.572, ('GRFFGGDRG', 'HLA-A*01:01'): 33764.332, ('GRKSAHKGF', 'HLA-A*01:01'): 33374.977, ('GRTQDENPV', 'HLA-A*01:01'): 31985.328, ('GSKYLATAS', 'HLA-A*01:01'): 29634.055, ('GSLPQKSHG', 'HLA-A*01:01'): 31245.67, ('GSPMARREL', 'HLA-A*01:01'): 29801.863, ('GTLSKIFKL', 'HLA-A*01:01'): 31416.641, ('GVDAQGTLS', 'HLA-A*01:01'): 21822.73, ('HARHGFLPR', 'HLA-A*01:01'): 27562.77, ('HFFKNIVTP', 'HLA-A*01:01'): 31079.244, ('HGFLPRHRD', 'HLA-A*01:01'): 35929.195, ('HGRTQDENP', 'HLA-A*01:01'): 32896.863, ('HGSKYLATA', 'HLA-A*01:01'): 25257.754, ('HHPARTAHY', 'HLA-A*01:01'): 13797.738, ('HKGFKGVDA', 'HLA-A*01:01'): 32444.189, ('HPARTAHYG', 'HLA-A*01:01'): 30605.928, ('HRDTGILDS', 'HLA-A*01:01'): 28518.939, ('HTIIYEAVC', 'HLA-A*01:01'): 23413.088, ('HYGSLPQKS', 'HLA-A*01:01'): 29772.008, ('IFKLGGRDS', 'HLA-A*01:01'): 33884.652, ('IGRFFGGDR', 'HLA-A*01:01'): 31376.129, ('IIYEAVCLH', 'HLA-A*01:01'): 24843.131, ('ILDSIGRFF', 'HLA-A*01:01'): 9863.752, ('IVTPRTPPP', 'HLA-A*01:01'): 31109.463, ('IYEAVCLHN', 'HLA-A*01:01'): 30276.92, ('KDSHHPART', 'HLA-A*01:01'): 33809.766, ('KGFKGVDAQ', 'HLA-A*01:01'): 33997.488, ('KGRKSAHKG', 'HLA-A*01:01'): 31678.871, ('KGVDAQGTL', 'HLA-A*01:01'): 31112.398, ('KIFKLGGRD', 'HLA-A*01:01'): 28736.641, ('KLGGRDSRS', 'HLA-A*01:01'): 31713.967, ('KNIVTPRTP', 'HLA-A*01:01'): 32355.387, ('KNMYKDSHH', 'HLA-A*01:01'): 32817.867, ('KRPSQRHGS', 'HLA-A*01:01'): 32696.377, ('KSAHKGFKG', 'HLA-A*01:01'): 31231.549, ('KSHGRTQDE', 'HLA-A*01:01'): 30463.646, ('KYLATASTM', 'HLA-A*01:01'): 30408.09, ('LATASTMDH', 'HLA-A*01:01'): 25452.285, ('LDSIGRFFG', 'HLA-A*01:01'): 32662.873, ('LGGRDSRSG', 'HLA-A*01:01'): 33970.43, ('LHNDRTTIP', 'HLA-A*01:01'): 32411.842, ('LPQKSHGRT', 'HLA-A*01:01'): 30876.816, ('LPRHRDTGI', 'HLA-A*01:01'): 32445.613, ('LSKIFKLGG', 'HLA-A*01:01'): 27659.91, ('LVISLIVES', 'HLA-A*01:01'): 28728.174, ('MARRELVIS', 'HLA-A*01:01'): 31353.307, ('MDHARHGFL', 'HLA-A*01:01'): 26452.84, ('MYKDSHHPA', 'HLA-A*01:01'): 21917.734, ('NIVTPRTPP', 'HLA-A*01:01'): 36242.363, ('NMYKDSHHP', 'HLA-A*01:01'): 32188.27, ('NPVVHFFKN', 'HLA-A*01:01'): 33140.523, ('PARTAHYGS', 'HLA-A*01:01'): 31889.75, ('PGHTIIYEA', 'HLA-A*01:01'): 27056.352, ('PKNMYKDSH', 'HLA-A*01:01'): 29087.582, ('PMARRELVI', 'HLA-A*01:01'): 27396.83, ('PPPSQGKGR', 'HLA-A*01:01'): 33229.676, ('PPSQGKGRK', 'HLA-A*01:01'): 33433.273, ('PQKSHGRTQ', 'HLA-A*01:01'): 36553.656, ('PRHRDTGIL', 'HLA-A*01:01'): 32165.867, ('PRTPPPSQG', 'HLA-A*01:01'): 36320.004, ('PSQGKGRKS', 'HLA-A*01:01'): 29472.758, ('PSQRHGSKY', 'HLA-A*01:01'): 552.14484, ('PVVHFFKNI', 'HLA-A*01:01'): 31549.891, ('QDENPVVHF', 'HLA-A*01:01'): 33366.957, ('QGKGRKSAH', 'HLA-A*01:01'): 32009.1, ('QGTLSKIFK', 'HLA-A*01:01'): 30763.568, ('QKRPSQRHG', 'HLA-A*01:01'): 31859.475, ('QKSHGRTQD', 'HLA-A*01:01'): 34106.02, ('QRHGSKYLA', 'HLA-A*01:01'): 25944.363, ('RDSRSGSPM', 'HLA-A*01:01'): 26912.316, ('RDTGILDSI', 'HLA-A*01:01'): 32451.338, ('RELVISLIV', 'HLA-A*01:01'): 26146.127, ('RFFGGDRGA', 'HLA-A*01:01'): 31706.709, ('RGAPKNMYK', 'HLA-A*01:01'): 22011.83, ('RHGFLPRHR', 'HLA-A*01:01'): 31218.834, ('RHGSKYLAT', 'HLA-A*01:01'): 32559.775, ('RHRDTGILD', 'HLA-A*01:01'): 28798.781, ('RKSAHKGFK', 'HLA-A*01:01'): 35683.336, ('RPSQRHGSK', 'HLA-A*01:01'): 31601.775, ('RRELVISLI', 'HLA-A*01:01'): 31098.012, ('RSGSPMARR', 'HLA-A*01:01'): 31929.006, ('RTAHYGSLP', 'HLA-A*01:01'): 19736.301, ('RTPPPSQGK', 'HLA-A*01:01'): 29869.498, ('RTQDENPVV', 'HLA-A*01:01'): 18235.035, ('SAHKGFKGV', 'HLA-A*01:01'): 33235.031, ('SGSPMARRE', 'HLA-A*01:01'): 32687.271, ('SHGRTQDEN', 'HLA-A*01:01'): 30508.158, ('SHHPARTAH', 'HLA-A*01:01'): 32420.652, ('SIGRFFGGD', 'HLA-A*01:01'): 27930.443, ('SKIFKLGGR', 'HLA-A*01:01'): 34817.629, ('SKYLATAST', 'HLA-A*01:01'): 31816.48, ('SLPQKSHGR', 'HLA-A*01:01'): 34400.605, ('SPMARRELV', 'HLA-A*01:01'): 29256.816, ('SQGKGRKSA', 'HLA-A*01:01'): 33573.285, ('SQKRPSQRH', 'HLA-A*01:01'): 34247.672, ('SQRHGSKYL', 'HLA-A*01:01'): 33573.219, ('SRSGSPMAR', 'HLA-A*01:01'): 30905.158, ('STMDHARHG', 'HLA-A*01:01'): 30898.145, ('STPGHTIIY', 'HLA-A*01:01'): 9019.3291, ('TAHYGSLPQ', 'HLA-A*01:01'): 32976.52, ('TASTMDHAR', 'HLA-A*01:01'): 30266.439, ('TGILDSIGR', 'HLA-A*01:01'): 34089.176, ('TIIYEAVCL', 'HLA-A*01:01'): 30612.641, ('TLSKIFKLG', 'HLA-A*01:01'): 30218.852, ('TMDHARHGF', 'HLA-A*01:01'): 11034.99, ('TPGHTIIYE', 'HLA-A*01:01'): 32463.441, ('TPPPSQGKG', 'HLA-A*01:01'): 31558.016, ('TPRTPPPSQ', 'HLA-A*01:01'): 36732.82, ('TQDENPVVH', 'HLA-A*01:01'): 22163.492, ('VCLHNDRTT', 'HLA-A*01:01'): 30707.113, ('VDAQGTLSK', 'HLA-A*01:01'): 24631.281, ('VHFFKNIVT', 'HLA-A*01:01'): 34133.156, ('VTPRTPPPS', 'HLA-A*01:01'): 26918.527, ('VVHFFKNIV', 'HLA-A*01:01'): 29944.451, ('YEAVCLHND', 'HLA-A*01:01'): 31620.496, ('YGSLPQKSH', 'HLA-A*01:01'): 33408.156, ('YKDSHHPAR', 'HLA-A*01:01'): 35071.301, ('YLATASTMD', 'HLA-A*01:01'): 21354.158, ('AHKGFKGVD', 'H-2-Ld'): 27314.703, ('AHYGSLPQK', 'H-2-Ld'): 31893.553, ('APKNMYKDS', 'H-2-Ld'): 34618.309, ('AQGTLSKIF', 'H-2-Ld'): 38435.066, ('ARHGFLPRH', 'H-2-Ld'): 19927.93, ('ARRELVISL', 'H-2-Ld'): 15375.162, ('ARTAHYGSL', 'H-2-Ld'): 9305.0654, ('ASQKRPSQR', 'H-2-Ld'): 31757.428, ('ASTMDHARH', 'H-2-Ld'): 42946.086, ('ASTPGHTII', 'H-2-Ld'): 32054.064, ('ATASTMDHA', 'H-2-Ld'): 39668.59, ('AVCLHNDRT', 'H-2-Ld'): 39340.188, ('CLHNDRTTI', 'H-2-Ld'): 33071.824, ('DAQGTLSKI', 'H-2-Ld'): 37543.109, ('DENPVVHFF', 'H-2-Ld'): 11366.467, ('DHARHGFLP', 'H-2-Ld'): 39231.125, ('DRGAPKNMY', 'H-2-Ld'): 41193.184, ('DSHHPARTA', 'H-2-Ld'): 42843.324, ('DSIGRFFGG', 'H-2-Ld'): 28096.723, ('DSRSGSPMA', 'H-2-Ld'): 40694.168, ('DTGILDSIG', 'H-2-Ld'): 42419.77, ('EAVCLHNDR', 'H-2-Ld'): 39104.793, ('ELVISLIVE', 'H-2-Ld'): 37108.797, ('ENPVVHFFK', 'H-2-Ld'): 5590.8853, ('FFGGDRGAP', 'H-2-Ld'): 37881.863, ('FFKNIVTPR', 'H-2-Ld'): 37029.465, ('FGGDRGAPK', 'H-2-Ld'): 22425.326, ('FKGVDAQGT', 'H-2-Ld'): 38413.262, ('FKLGGRDSR', 'H-2-Ld'): 28917.314, ('FKNIVTPRT', 'H-2-Ld'): 34675.469, ('FLPRHRDTG', 'H-2-Ld'): 35887.039, ('GAPKNMYKD', 'H-2-Ld'): 33100.82, ('GDRGAPKNM', 'H-2-Ld'): 27005.953, ('GFKGVDAQG', 'H-2-Ld'): 34020.582, ('GFLPRHRDT', 'H-2-Ld'): 33069.047, ('GGDRGAPKN', 'H-2-Ld'): 36673.422, ('GGRDSRSGS', 'H-2-Ld'): 39425.82, ('GHTIIYEAV', 'H-2-Ld'): 28450.537, ('GILDSIGRF', 'H-2-Ld'): 31921.061, ('GKGRKSAHK', 'H-2-Ld'): 40246.16, ('GRDSRSGSP', 'H-2-Ld'): 37619.16, ('GRFFGGDRG', 'H-2-Ld'): 34098.375, ('GRKSAHKGF', 'H-2-Ld'): 24809.463, ('GRTQDENPV', 'H-2-Ld'): 41650.902, ('GSKYLATAS', 'H-2-Ld'): 40106.691, ('GSLPQKSHG', 'H-2-Ld'): 36105.129, ('GSPMARREL', 'H-2-Ld'): 19205.23, ('GTLSKIFKL', 'H-2-Ld'): 29537.869, ('GVDAQGTLS', 'H-2-Ld'): 39088.836, ('HARHGFLPR', 'H-2-Ld'): 38182.98, ('HFFKNIVTP', 'H-2-Ld'): 33215.547, ('HGFLPRHRD', 'H-2-Ld'): 31334.416, ('HGRTQDENP', 'H-2-Ld'): 36135.305, ('HGSKYLATA', 'H-2-Ld'): 13534.686, ('HHPARTAHY', 'H-2-Ld'): 36681.887, ('HKGFKGVDA', 'H-2-Ld'): 34834.965, ('HPARTAHYG', 'H-2-Ld'): 10198.595, ('HRDTGILDS', 'H-2-Ld'): 28307.367, ('HTIIYEAVC', 'H-2-Ld'): 37192.941, ('HYGSLPQKS', 'H-2-Ld'): 41107.355, ('IFKLGGRDS', 'H-2-Ld'): 39277.992, ('IGRFFGGDR', 'H-2-Ld'): 18694.189, ('IIYEAVCLH', 'H-2-Ld'): 28468.396, ('ILDSIGRFF', 'H-2-Ld'): 13098.865, ('IVTPRTPPP', 'H-2-Ld'): 37031.125, ('IYEAVCLHN', 'H-2-Ld'): 32423.188, ('KDSHHPART', 'H-2-Ld'): 40136.27, ('KGFKGVDAQ', 'H-2-Ld'): 22394.785, ('KGRKSAHKG', 'H-2-Ld'): 37143.848, ('KGVDAQGTL', 'H-2-Ld'): 3635.575, ('KIFKLGGRD', 'H-2-Ld'): 38491.078, ('KLGGRDSRS', 'H-2-Ld'): 27778.127, ('KNIVTPRTP', 'H-2-Ld'): 39630.816, ('KNMYKDSHH', 'H-2-Ld'): 40769.023, ('KRPSQRHGS', 'H-2-Ld'): 38997.648, ('KSAHKGFKG', 'H-2-Ld'): 41273.52, ('KSHGRTQDE', 'H-2-Ld'): 29496.996, ('KYLATASTM', 'H-2-Ld'): 33859.07, ('LATASTMDH', 'H-2-Ld'): 37431.957, ('LDSIGRFFG', 'H-2-Ld'): 30446.162, ('LGGRDSRSG', 'H-2-Ld'): 31206.242, ('LHNDRTTIP', 'H-2-Ld'): 39762.332, ('LPQKSHGRT', 'H-2-Ld'): 3915.7581, ('LPRHRDTGI', 'H-2-Ld'): 31037.451, ('LSKIFKLGG', 'H-2-Ld'): 32769.391, ('LVISLIVES', 'H-2-Ld'): 38046.488, ('MARRELVIS', 'H-2-Ld'): 41631.602, ('MDHARHGFL', 'H-2-Ld'): 3342.0251, ('MYKDSHHPA', 'H-2-Ld'): 38494.09, ('NIVTPRTPP', 'H-2-Ld'): 43070.938, ('NMYKDSHHP', 'H-2-Ld'): 30510.805, ('NPVVHFFKN', 'H-2-Ld'): 21938.521, ('PARTAHYGS', 'H-2-Ld'): 27730.668, ('PGHTIIYEA', 'H-2-Ld'): 24000.609, ('PKNMYKDSH', 'H-2-Ld'): 38076.727, ('PMARRELVI', 'H-2-Ld'): 32796.559, ('PPPSQGKGR', 'H-2-Ld'): 37273.688, ('PPSQGKGRK', 'H-2-Ld'): 26768.793, ('PQKSHGRTQ', 'H-2-Ld'): 39839.008, ('PRHRDTGIL', 'H-2-Ld'): 35605.219, ('PRTPPPSQG', 'H-2-Ld'): 42786.652, ('PSQGKGRKS', 'H-2-Ld'): 38715.059, ('PSQRHGSKY', 'H-2-Ld'): 38711.035, ('PVVHFFKNI', 'H-2-Ld'): 31737.959, ('QDENPVVHF', 'H-2-Ld'): 29118.584, ('QGKGRKSAH', 'H-2-Ld'): 25642.346, ('QGTLSKIFK', 'H-2-Ld'): 22144.984, ('QKRPSQRHG', 'H-2-Ld'): 39108.637, ('QKSHGRTQD', 'H-2-Ld'): 30513.018, ('QRHGSKYLA', 'H-2-Ld'): 20631.082, ('RDSRSGSPM', 'H-2-Ld'): 28487.732, ('RDTGILDSI', 'H-2-Ld'): 28967.66, ('RELVISLIV', 'H-2-Ld'): 31536.053, ('RFFGGDRGA', 'H-2-Ld'): 34794.855, ('RGAPKNMYK', 'H-2-Ld'): 21950.471, ('RHGFLPRHR', 'H-2-Ld'): 34739.254, ('RHGSKYLAT', 'H-2-Ld'): 35622.406, ('RHRDTGILD', 'H-2-Ld'): 34728.453, ('RKSAHKGFK', 'H-2-Ld'): 28260.137, ('RPSQRHGSK', 'H-2-Ld'): 3896.2722, ('RRELVISLI', 'H-2-Ld'): 26155.879, ('RSGSPMARR', 'H-2-Ld'): 36704.914, ('RTAHYGSLP', 'H-2-Ld'): 38326.684, ('RTPPPSQGK', 'H-2-Ld'): 42051.82, ('RTQDENPVV', 'H-2-Ld'): 39463.891, ('SAHKGFKGV', 'H-2-Ld'): 30009.348, ('SGSPMARRE', 'H-2-Ld'): 23316.693, ('SHGRTQDEN', 'H-2-Ld'): 32204.85, ('SHHPARTAH', 'H-2-Ld'): 18621.148, ('SIGRFFGGD', 'H-2-Ld'): 18066.852, ('SKIFKLGGR', 'H-2-Ld'): 41036.109, ('SKYLATAST', 'H-2-Ld'): 28031.926, ('SLPQKSHGR', 'H-2-Ld'): 39916.816, ('SPMARRELV', 'H-2-Ld'): 3711.8298, ('SQGKGRKSA', 'H-2-Ld'): 28302.697, ('SQKRPSQRH', 'H-2-Ld'): 42321.172, ('SQRHGSKYL', 'H-2-Ld'): 39098.715, ('SRSGSPMAR', 'H-2-Ld'): 15313.73, ('STMDHARHG', 'H-2-Ld'): 39151.102, ('STPGHTIIY', 'H-2-Ld'): 36597.641, ('TAHYGSLPQ', 'H-2-Ld'): 38276.57, ('TASTMDHAR', 'H-2-Ld'): 38764.195, ('TGILDSIGR', 'H-2-Ld'): 38168.488, ('TIIYEAVCL', 'H-2-Ld'): 24241.178, ('TLSKIFKLG', 'H-2-Ld'): 34460.957, ('TMDHARHGF', 'H-2-Ld'): 11118.251, ('TPGHTIIYE', 'H-2-Ld'): 11598.688, ('TPPPSQGKG', 'H-2-Ld'): 26560.375, ('TPRTPPPSQ', 'H-2-Ld'): 35927.484, ('TQDENPVVH', 'H-2-Ld'): 36136.891, ('VCLHNDRTT', 'H-2-Ld'): 22993.828, ('VDAQGTLSK', 'H-2-Ld'): 37537.234, ('VHFFKNIVT', 'H-2-Ld'): 38501.836, ('VTPRTPPPS', 'H-2-Ld'): 40762.996, ('VVHFFKNIV', 'H-2-Ld'): 23935.875, ('YEAVCLHND', 'H-2-Ld'): 13513.598, ('YGSLPQKSH', 'H-2-Ld'): 39397.105, ('YKDSHHPAR', 'H-2-Ld'): 38144.0, ('YLATASTMD', 'H-2-Ld'): 14650.152}

def process_results(results, alleles):
    processed_result = {}
