import csv
import argparse

def read_snps(snps_file):
    snps = []
    with open(snps_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            snps.append((row[0], int(row[1])))
    return snps

def read_gff3(gff3_file):
    gff3_data = []
    with open(gff3_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            gff3_data.append((row[0], int(row[3]), int(row[4]), row))
    return gff3_data

def find_genes(snps, gff3_data):
    genes = []
    for snp in snps:
        for gff3_row in gff3_data:
            if snp[0] == gff3_row[0] and gff3_row[1] <= snp[1] <= gff3_row[2]:
                genes.append(gff3_row[3])
    return genes

def write_output(output_file, genes):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(genes)

def main(args):
    snps = read_snps(args.snps_file)
    gff3_data = read_gff3(args.gff3_file)
    genes = find_genes(snps, gff3_data)
    write_output(args.output_file, genes)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find genes encompassing SNP loci.')
    parser.add_argument('snps_file', help='Path to the SNP loci file.')
    parser.add_argument('gff3_file', help='Path to the GFF3 file.')
    parser.add_argument('output_file', help='Path to the output file.')
    args = parser.parse_args()
    main(args)

