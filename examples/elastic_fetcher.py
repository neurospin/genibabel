"""
Genetic ElasticSearch fetcher
=============================

Credit: A Grigis
"""


# Imports
from genibabel import MetaGen
from pprint import pprint

metagen = MetaGen(url="https://biothings.intra.cea.fr",  verify_certs=False)
metagen.status()

pprint(metagen.get_genes(gene="FOXP2"))
print([item["hgnc_name"] for item in metagen.get_genes(chromosome="7").values()])
print([item["hgnc_name"] for item in metagen.get_genes(
    chromosome="22", pos_low=11124337, pos_up=12626642).values()])
print([item["hgnc_name"] for item in metagen.get_genes(pathway="PILON_KLF1_TARGETS_UP").values()])
print([item["hgnc_name"] for item in metagen.get_genes(cpg="cg07298940").values()])
print(metagen.get_snps(chromosome="7", pos_low=114086327, pos_up=114693772).keys())
snp_name = "rs619251"
snp_info = metagen.get_snps(name=snp_name)
pprint(snp_info)
for ens_name in snp_info[snp_name]["related_genes"]:
    pprint(metagen.get_genes(name=ens_name)[ens_name]["hgnc_name"])

































