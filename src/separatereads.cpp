#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#include <string.h>
#include<vector>
#include<fstream>

using namespace std;
char ch;
double flag_singal=0,flag_read=0,flag_num=1,flag_invalid=0,flag_sup=0,flag_rev=0,invalid_read_num=0,valid_read_num=0;
//int genome1[813184]={0},genome2[316620]={0},genome3[1531933]={0},genome4[439888]={0},genome0[230218]={0},genome5[85779]={0};
//int genome6[576874]={0},genome7[270161]={0},genome8[1090940]={0},genome9[562643]={0},genome10[745751]={0},genome11[666816]={0};

//int genome12[1078177]={0},genome13[924431]={0},genome14[784333]={0},genome15[1091291]={0},genome16[948066]={0};
int genome[200000000]={0};
string pos_str;
int POS=0,read_len1=0,read_len2=0,read_num=0;
string SN,LN,ID,PN,VN,CL,gi,num;
double num_M=0,num_I=0,num_D=0,num_S=0,num_H=0,num_X=0,num_equal=0,base_count=0,alignbase=0,aligncount=0;
double reserve=0;
double alignment=0;
double similarity=0;
double coverage=0;
int i=0;
int length[1000000]={0};
void f5();
int read[100000]={0};
FILE *f_fp;
string method="";
void rev_1();
int flaglen=0;
double genomelen=0;
int flag_tab=0;
vector<string> genomenamevec;
vector<string> genomelenvec;
int readslist[2000000]={0};

int read_genome_num=0;
ofstream fout;
void breakpoint()
{

}

void cigar(FILE* file)
{
	int read_index=0;
	string str_readname="";
	ch=fgetc(file);
	int flag=0;
	while (!feof(file))
	{
		int flag_invalid=0;
		
		if(ch=='_'&&flag==0)
		{
			
			read_index=atoi(str_readname.c_str());
			str_readname.clear();
			readslist[read_index]=1;
			while(!feof(file))
			{
				ch=fgetc(file);
				if(ch=='\n')
				{
					flag=1;
					break;
				}
			}
			
		}
		else if(ch!='>')
		{
			str_readname+=ch;
		}
		if(flag==1)
		{
			while(!feof(file))
			{
				ch=fgetc(file);
				if(ch=='\n')
				{
					flag=0;
					break;
				}
			}
		}
		
		ch=fgetc(file);
	}
	fclose(f_fp);

}



void f2(FILE *f_fp)
{
	string str_readname="";
	ch=fgetc(f_fp);
	int read_index=0;

	while (!feof(f_fp))
	{
		int flag_invalid=0;
		
		if(ch=='\n')
		{
			
			read_index=atoi(str_readname.c_str());
			str_readname.clear();
			if(readslist[read_index]==0)
			{
				fout<<">"<<read_index<<endl;
				while(!feof(f_fp))
				{
					ch=fgetc(f_fp);
					fout<<ch;
					if(ch=='\n')
					{
						break;
					}
				}
			}
			else
			{
				while(!feof(f_fp))
				{
					ch=fgetc(f_fp);
					if(ch=='\n')
					{
						break;
					}
				}
			}
		}
		else if(ch!='>')
		{
			str_readname+=ch;
		}
		
		ch=fgetc(f_fp);
	}
	fclose(f_fp);

}



int main(int argc,char * argv[])
{
	//argv[1] corrected.fasta
	string filename="0";
	filename=argv[1];
	const char* filename2;
	filename2=filename.c_str();
	f_fp=fopen(filename2,"r");
	cigar(f_fp);



	filename=argv[2];
	const char* filename1;
	filename1=filename.c_str();
	f_fp=fopen(filename1,"r");

	
	string filename4="0";
	filename4=argv[3];
	const char* filename5;
	filename5=filename4.c_str();
	fout.open(filename5,ios::trunc);
	f2(f_fp);
	
	
	return 0;
}