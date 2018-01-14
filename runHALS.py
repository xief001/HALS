#!/usr/bin/python

import os
import argparse
import shutil
import datetime

parser = argparse.ArgumentParser(description='runHALC.py')
parser.add_argument('long_read_path', metavar='long_read.fa', help="The path to long_read.fa")
parser.add_argument("-f1",help="Fraction value to distinguish between the cases (i)/(ii) and (iii).(0.5)", default=0.5,type=float)
parser.add_argument('-f2',help="Fraction value to distinguish between the cases (i) and (ii).(0.5)", default=0.5,type=float)
parser.add_argument('-d1', help="Difference value of alignment identities to find the correct aligned path.(0.05)", default=0.05,type=float)
parser.add_argument('-d2', help="Difference value of expected amounts of aligned long reads to find the correct aligned path.(0.2)", default=0.2,type=float)
args = parser.parse_args()

# Default Parameters#####################################
temp_dir = './temp'
output_dir = './output'
prefix = 'HALS'
repeat_free_mode = False

if os.path.exists(temp_dir + '/step1'):
	if os.path.exists(temp_dir + '/step2'):
		print 'WARNING: ' + temp_dir + '/step2' + ' was found. Automatically started from step5'
		shutil.rmtree(temp_dir + '/step2')
		start_from_step = 2
	else:
		print 'WARNING: ' + temp_dir + '/step1' + ' was found. Automatically started from step1'
		shutil.rmtree(temp_dir + '/step1')
		start_from_step = 1
else:
	start_from_step = 1
# Parameters Analyzing###################################
long_read_path = args.long_read_path

if args.f1 > 1 or args.f1 < 0:
	print 'ERROR: argument -f1  INVALID INPUT PARAMETER (should be between 0 and 1)!'
	exit(-1)
if args.f2 > 1 or args.f2 < 0:
	print 'ERROR: argument -f2  INVALID INPUT PARAMETER (should be between 0 and 1)!'
	exit(-1)
if args.d1 > 1 or args.d1 < 0:
	print 'ERROR: argument -d1  INVALID INPUT PARAMETER (should be between 0 and 1)!'
	exit(-1)
if args.d2 > 1 or args.d2 < 0:
	print 'ERROR: argument -d2  INVALID INPUT PARAMETER (should be between 0 and 1)!'
	exit(-1)

start_time = datetime.datetime.now()
print start_time

# Step 1 MECAT1#########################
if start_from_step <= 1:
	print'''
/////STEP 1 STARTED//////////////////////////////////////////////////////////////////////////////////////////////////'''
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	if not os.path.exists(temp_dir):
		os.makedirs(temp_dir)

	if os.path.exists(temp_dir + '/step1'):
		print 'ERROR: ' + temp_dir + '/step1' + ' already exist, please delete it before running step 1'
		exit(-1)
	else:
		os.mkdir(temp_dir + '/step1')

	preread_command = 'preread ' + long_read_path + ' ' + temp_dir + '/step1/' + 'allreads.fasta ' 

	print 'Running command: ' + preread_command
	err = os.system(preread_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun preread:' + os.strerror(err)
		exit(-1)
	

#################################
	mecat2pw1_command = 'mecat2pw -j 1 -t 16 -g 1 -x 0 -d ' + temp_dir + '/step1/' + 'allreads.fasta ' + ' -o ' + temp_dir + '/step1/' + 'allreads.fasta.m4 ' + ' -w ' + temp_dir + '/step1/' + 'tmpfold '

	print 'Running command: ' + mecat2pw1_command
	err = os.system(mecat2pw1_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun mecat2pw1:' + os.strerror(err)
		exit(-1)
################################
	rm1_command = 'rm -rf ' + temp_dir + '/step1/' + 'tmpfold '

	print 'Running command: ' + rm1_command
	err = os.system(rm1_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun rm1:' + os.strerror(err)
		exit(-1)

#####################################
	bronkerboschadj1_command = 'bronkerboschadj ' + temp_dir + '/step1/' + 'allreads.fasta.m4 ' + temp_dir + '/step1/' + 'clique1.txt ' +  temp_dir + '/step1/' + 'edge1.txt 3 '

	print 'Running command: ' + bronkerboschadj1_command
	err = os.system(bronkerboschadj1_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun bronkerboschadj1:' + os.strerror(err)
		exit(-1)

#####################################
	HALS1_command = 'HALS 1 -c ' + temp_dir + '/step1/' + 'clique1.txt ' + ' -e ' + temp_dir + '/step1/' + 'edge1.txt ' + ' -r ' + temp_dir + '/step1/' + ' allreads.fasta ' + ' -m ' + temp_dir + '/step1/' +' allreads.fasta.m4 ' + ' -a ' + temp_dir + '/step1/' +' realireads1.fasta ' + ' -d ' + temp_dir + '/step1/' + 'deletepairs1.txt '


	print 'Running command: ' + HALS1_command
	err = os.system(HALS1_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun HALS1:' + os.strerror(err)
		exit(-1)
####################################
	
	mecat2pw2_command = ' mecat2pw -j 1 -t 16 -g 1 -x 0 -d ' + temp_dir + '/step1/' + 'realireads1.fasta ' + ' -o ' + temp_dir + '/step1/' + 'realireads1.fasta.m4 ' + ' -w ' + temp_dir + '/step1/' + 'tmpfold '


	print 'Running command: ' + mecat2pw2_command
	err = os.system(mecat2pw2_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun mecat2pw2:' + os.strerror(err)
		exit(-1)

####################################
	rm2_command = 'rm -rf ' + temp_dir + '/step1/' + 'tmpfold '

	print 'Running command: ' + rm2_command
	err = os.system(rm2_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun rm2:' + os.strerror(err)
		exit(-1)

#################################
	
	addm42MECATm41_command = 'addm42MECATm4 ' + temp_dir + '/step1/' + 'allreads.fasta.m4 ' + temp_dir + '/step1/' + 'realireads1.fasta.m4 ' + temp_dir + '/step1/' + 'realireads1.fasta ' + temp_dir + '/step1/' + 'allreads.fasta ' +  temp_dir + '/step1/' + 'realireads1_.fasta.m4 '
	print 'Running command: ' + addm42MECATm41_command
	err = os.system(addm42MECATm41_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun addm42MECATm41:' + os.strerror(err)
		exit(-1)

###############################

	mecat2cns1_command = 'mecat2cns -x 0 -i 1 -t 16 -l 10 -c 3 ' + temp_dir + '/step1/' + 'realireads1_.fasta.m4 ' + temp_dir + '/step1/' + 'allreads.fasta ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta '
	print 'Running command: ' + mecat2cns1_command
	err = os.system(mecat2cns1_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun mecat2cns1:' + os.strerror(err)
		exit(-1)
#########################################
	print '''
/////STEP 1 DONE/////////////////////////////////////////////////////////////////////////////////////////////////////'''
# Step 2 Run Blasr###############################
if start_from_step <= 2:
	print '''
/////STEP 2 STARTED//////////////////////////////////////////////////////////////////////////////////////////////////'''
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	if not os.path.exists(temp_dir):
		os.makedirs(temp_dir)

	if os.path.exists(temp_dir + '/step2'):
		print 'ERROR: ' + temp_dir + '/step2' + ' already exist, please delete it before running step 2'
		exit(-1)
	else:
		os.mkdir(temp_dir + '/step2')
###########################

	separatereads_command = 'separatereads ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta ' + temp_dir + '/step1/' + 'allreads.fasta ' + temp_dir + '/step2/' + 'incorrectedreads.fasta '
	print 'Running command: ' + separatereads_command
	err = os.system(separatereads_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun separatereads:' + os.strerror(err)
		exit(-1)
#################################

	mecat2pw3_command = ' mecat2pw -j 1 -t 16 -g 1 -x 0 -d ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta ' + ' -o ' + temp_dir + '/step2/' + 'allreads0_corrected_filted1.fasta.m4 '+ ' -w ' + temp_dir + '/step2/' + 'tmpfold '
	print 'Running command: ' + mecat2pw3_command
	err = os.system(mecat2pw3_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun mecat2pw3:' + os.strerror(err)
		exit(-1)
###########################################

	rm3_command = 'rm -rf ' + temp_dir + '/step2/' + 'tmpfold '
	print 'Running command: ' + rm3_command
	err = os.system(rm3_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun rm3:' + os.strerror(err)
		exit(-1)

###########################################

	cat1_command = 'cat ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta '+ temp_dir + '/step2/' + 'incorrectedreads.fasta ' + '>' + temp_dir + '/step2/' + 'cor_incor.fasta '
	print 'Running command: ' + cat1_command
	err = os.system(cat1_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun cat1:' + os.strerror(err)
		exit(-1)
#############################################

	mecat2pw4_command = ' mecat2pw -j 1 -t 16 -g 1 -x 0 -d ' + temp_dir + '/step2/' + 'cor_incor.fasta ' + ' -o ' + temp_dir + '/step2/' + 'cor_incor.fasta.m4 '+ ' -w ' + temp_dir + '/step2/' + 'tmpfold '
	print 'Running command: ' + mecat2pw3_command
	err = os.system(mecat2pw3_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun mecat2pw3:' + os.strerror(err)
		exit(-1)

	rm4_command = 'rm -rf ' + temp_dir + '/step2/' + 'tmpfold '
	print 'Running command: ' + rm4_command
	err = os.system(rm4_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun rm4:' + os.strerror(err)
		exit(-1)

########################################
	bronkerboschadj2_command = 'bronkerboschadj ' + temp_dir + '/step2/' + 'allreads0_corrected_filted1.fasta.m4 ' + temp_dir + '/step2/' + 'clique2.txt ' +  temp_dir + '/step2/' + 'edge2.txt 3'
	print 'Running command: ' + bronkerboschadj2_command
	err = os.system(bronkerboschadj2_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun bronkerboschadj2:' + os.strerror(err)
		exit(-1)
############################################
	FN1=0

	FN1_command = 'FN1=$(wc -l < ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta '
	print 'Running command: ' + FN1_command
	err = os.system(FN1_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun FN1:' + os.strerror(err)
		exit(-1)


##########################################

	HALS2_command = 'HALS 2 $FN1 -c ' + temp_dir + '/step2/' + 'clique2.txt ' + ' -e ' + temp_dir + '/step2/' + 'edge2.txt ' + ' -r ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta ' + ' -m ' + temp_dir + '/step2/' +'allreads0_corrected_filted1.fasta.m4 ' + ' -de2 ' + temp_dir + '/step2/' +'deletepairs2.txt ' + ' -de3 ' + temp_dir + '/step2/' + 'deletepairs3.txt '+ ' -w ' + temp_dir + '/step2/' + 'cor_incor.fasta ' + ' -g ' + temp_dir + '/step2/' + 'cor_incor.fasta.m4 '+'-f1 '+args.f1+' -f2 '+args.f2+' -d1 '+args.d1+' -d2 '+args.d2
	print 'Running command: ' + HALS2_command
	err = os.system(HALS2_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun HALS2:' + os.strerror(err)
		exit(-1)
#########################################
	modifym4file2_command = 'modifym4file2 ' + temp_dir + '/step2/' + 'cor_incor.fasta.m4 '+ temp_dir + '/step2/' + 'deletepairs3.txt '+ temp_dir + '/step2/' +'corrected2.m4 '
	print 'Running command: ' + modifym4file2_command
	err = os.system(modifym4file2_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun modifym4file2:' + os.strerror(err)
		exit(-1)
######################################
	mecat2cns2_command = 'mecat2cns -x 0 -i 1 -t 16 -l 10 -c 3 ' + temp_dir + '/step2/' + 'corrected2.m4 ' + temp_dir + '/step2/' + 'cor_incor.fasta ' + temp_dir + '/step2/' + 'allreads0_corrected_filted2.fasta '
	print 'Running command: ' + mecat2cns2_command
	err = os.system(mecat2cns2_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun mecat2cns2:' + os.strerror(err)
		exit(-1)

##########################################

	filter_command = 'filter ' + temp_dir + '/step2/' + 'allreads0_corrected_filted2.fasta ' + FN1 + ' ' + temp_dir + '/step2/' + 'allreads0_corrected_filted3.fasta '
	print 'Running command: ' + filter_command
	err = os.system(filter_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun mecat2cns2:' + os.strerror(err)
		exit(-1)


############################################

	cat2_command = 'cat ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta '+ temp_dir + '/step2/' + 'incorrectedreads.fasta ' + '>' + temp_dir + '/step2/' + 'cor_incor.fasta '

	print 'Running command: ' + cat2_command
	err = os.system(cat2_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun cat2:' + os.strerror(err)
		exit(-1)



############################################

	write_corrected2_command = 'write_corrected2 '+ FN1 + temp_dir + '/step2/' + 'allreads0_corrected_filted2.fasta '+ temp_dir + '/step2/' + 'correctedreads2.fasta '
	print 'Running command: ' + write_corrected2_command
	err = os.system(write_corrected2_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun write_corrected2:' + os.strerror(err)
		exit(-1)

##############################################

	cat3_command = 'cat ' + temp_dir + '/step1/' + 'allreads0_corrected_filted1.fasta '+ temp_dir + '/step2/' + 'correctedreads2.fasta ' + '>' + output_dir + 'split_reads.fasta '
	print 'Running command: ' + cat3_command
	err = os.system(cat3_command)
	if err != 0:
		print 'ERROR: ' + 'Failed torun cat3:' + os.strerror(err)
		exit(-1)



#############################################
	full_trim_command = 'full_trim ' + output_dir + 'split_reads.fasta '+ temp_dir + '/step1/' + 'allreads.fasta '+ output_dir +'full_reads.fasta '  + output_dir +'trimmed_reads.fasta '
	print 'Running command: ' + full_trim_command
	err = os.system(full_trim_command)

	if err != 0:
		print 'ERROR: ' + 'Failed torun full_trim:' + os.strerror(err)
		exit(-1)
	print '''
###############################################

/////Finished!!! Results are stored in output folder/////////////////////////////////////////////////////////////////'''

end_time = datetime.datetime.now()
print end_time
time_cost = end_time - start_time
print 'Running time: ' + str(time_cost)

