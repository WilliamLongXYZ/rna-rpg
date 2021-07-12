import random
import time


somatic_cell_count = 1
somatic_chromosome_count = somatic_cell_count*(22*2)+2
second_sex_chromosome = random.randint(0,1)
sex_chromosome_label = "XX" if second_sex_chromosome == 0 else "XY"
if sex_chromosome_label == 'XX': sex = 'Male'
if sex_chromosome_label == 'XY': sex = 'Female'
dna_condensed = False

def calculate_total_chromosomes(cell_count, chromosome_count):
	chromosome_count = cell_count*((22*2)+2)

def step():
	input("Press [ENTER] to step to the next section.\n\n")

def G0():
	pass

def G1():
	print("Interphase: Growth"); step()

def S():
	print("Interphase: Synthesis"); step()

def G2():
	print("Interphase: Growth"); step()

def interphase():
	print("Interphase\n")
	G1(); S(); G2()
	length = random.randint(64800, 72000) # LENGTH OF TIME THIS PHASE TAKES
	global somatic_chromosome_count
	somatic_chromosome_count *= 2
	print("End of Interphase"); step()

def cytokenesis():
    print("Cytokenesis")
    step()

class Cell:
    class GermCell:
        pass
    class DNA:
        def to_rna(sequence):
            pass
        class Gene:
            class Allele:
                def __init__(self):
                    self.blood_type = None
                    self.eye_color = None

                def determine_blood_type(self, allele_one, allele_two):
                    self.blood_type = allele_one + allele_two
    class RNA():
        pass

class SomaticCell(Cell):
    def prophase():
        print("Prophase")
        dna_condensed = True
        print("Chromatin condenses")
        step()

    def metaphase():
        print("Metaphase"); step()

    def anaphase():
        print("Anaphase"); step()

    def telophase():
        print("Telophase")
        global somatic_cell_count, somatic_chromosome_count
        somatic_cell_count *= 2; print("Cell splits")
        somatic_chromosome_count /= 2
        step()

    def cytokenesis():
        print("Cytokenesis"); step()

    def mitosis(self):
        print("Mitosis\n")
        length = 7200 # LENGTH OF TIME THIS PHASE TAKES
        SomaticCell.prophase(); self.metaphase(); self.anaphase(); self.telophase(); self.cytokenesis()
        print("End of Mitosis")
        step()

    def cell_division(self):
        print("Somatic Cell Division\n")
        self.mitosis(self); interphase()
        print("End of Somatic Cell Division")
        step()
