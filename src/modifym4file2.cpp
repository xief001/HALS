#include<stdio.h>
#include<iostream>
#include<string>
#include<fstream>
#include<stdlib.h>
#include <vector>
using namespace std;
FILE* f_orim4;
FILE* f_ali;
FILE* f_del;
FILE* f_newm4;

typedef struct m4info
{
	string readname1;
	int start1;
	int end1;
	string info3;
	string info4;
	string info5;
	string readname2;
	int start2;
	int end2;
	string info8;
	string info9;
	string info12;
	string info13;
}m4info;

typedef struct m4info_node
{
	m4info info;
	struct m4info_node * next;
}m4info_node;

typedef struct delpair
{
	string readname1;
	string readname2;
}delpair;

typedef struct delpair_node
{
	delpair info;
	struct delpair_node * next;
}delpair_node;

vector <m4info> orim4list;
vector <m4info> alilist;
vector <delpair> delpairlist;

void readorim4file()
{
	char ch;
	ch= fgetc(f_orim4);
	string readname="";
	string str="";
	int flag=0;
	int count=0;
	m4info tmpm4info;
	while(!feof(f_orim4))
	{
		if(ch==-1)
		{
			break;
		}
		if(ch=='\t'&&flag==0)
		{
			tmpm4info.readname1=str.c_str();
			flag=1;
			str.clear();
		}
		else if(ch=='\t'&&flag==1)
		{
			tmpm4info.readname2=str.c_str();
			flag=2;
			str.clear();
		}
		else if(ch=='\t'&&flag==2)
		{
			tmpm4info.info3=str.c_str();
			flag=3;
			str.clear();
		}
		else if(ch=='\t'&&flag==3)
		{
			tmpm4info.info4=str.c_str();
			flag=4;
			str.clear();
		}
		else if(ch=='\t'&&flag==4)
		{
			tmpm4info.info5=str.c_str();
			flag=5;
			str.clear();
		}
		else if(ch=='\t'&&flag==5)
		{
			tmpm4info.start1=atof(str.c_str());
			flag=6;
			str.clear();
		}
		else if(ch=='\t'&&flag==6)
		{
			tmpm4info.end1=atof(str.c_str());
			flag=7;
			str.clear();
		}
		else if(ch=='\t'&&flag==7)
		{
			tmpm4info.info8=str.c_str();
			flag=8;
			str.clear();
		}
		else if(ch=='\t'&&flag==8)
		{
			tmpm4info.info9=str.c_str();
			flag=9;
			str.clear();
		}
		else if(ch=='\t'&&flag==9)
		{
			tmpm4info.start2=atof(str.c_str());
			flag=10;
			str.clear();
		}
		else if(ch=='\t'&&flag==10)
		{
			tmpm4info.end2=atof(str.c_str());
			flag=11;
			str.clear();
		}
		else if(ch=='\t'&&flag==11)
		{
			tmpm4info.info12=str.c_str();
			flag=12;
			str.clear();
		}
		else if(ch=='\n')
		{
			tmpm4info.info13=str.c_str();
			flag=0;
			str.clear();
			orim4list.push_back(tmpm4info);
		}
		else
		{
			str+=ch;
		}
		ch=fgetc(f_orim4);
	}
	fclose(f_orim4);
}

void readalim4file()
{
	char ch;
	ch= fgetc(f_ali);
	string readname="";
	string str="";
	int flag=0;
	int count=0;
	m4info tmpm4info;
	while(!feof(f_ali))
	{
		if(ch==-1)
		{
			break;
		}
		if(ch=='\t'&&flag==0)
		{
			tmpm4info.readname1=str.c_str();
			flag=1;
			str.clear();
		}
		else if(ch=='\t'&&flag==1)
		{
			tmpm4info.readname2=str.c_str();
			flag=2;
			str.clear();
		}
		else if(ch=='\t'&&flag==2)
		{
			tmpm4info.info3=str.c_str();
			flag=3;
			str.clear();
		}
		else if(ch=='\t'&&flag==3)
		{
			tmpm4info.info4=str.c_str();
			flag=4;
			str.clear();
		}
		else if(ch=='\t'&&flag==4)
		{
			tmpm4info.info5=str.c_str();
			flag=5;
			str.clear();
		}
		else if(ch=='\t'&&flag==5)
		{
			tmpm4info.start1=atof(str.c_str());
			flag=6;
			str.clear();
		}
		else if(ch=='\t'&&flag==6)
		{
			tmpm4info.end1=atof(str.c_str());
			flag=7;
			str.clear();
		}
		else if(ch=='\t'&&flag==7)
		{
			tmpm4info.info8=str.c_str();
			flag=8;
			str.clear();
		}
		else if(ch=='\t'&&flag==8)
		{
			tmpm4info.info9=str.c_str();
			flag=9;
			str.clear();
		}
		else if(ch=='\t'&&flag==9)
		{
			tmpm4info.start2=atof(str.c_str());
			flag=10;
			str.clear();
		}
		else if(ch=='\t'&&flag==10)
		{
			tmpm4info.end2=atof(str.c_str());
			flag=11;
			str.clear();
		}
		else if(ch=='\t'&&flag==11)
		{
			tmpm4info.info12=str.c_str();
			flag=12;
			str.clear();
		}
		else if(ch=='\n')
		{
			tmpm4info.info13=str.c_str();
			flag=0;
			str.clear();
			alilist.push_back(tmpm4info);
		}
		else
		{
			str+=ch;
		}
		ch=fgetc(f_ali);
	}
	fclose(f_ali);
}

void readdelfile()
{
	char ch;
	ch= fgetc(f_del);
	string readname="";
	string str="";
	int count=0;
	delpair tmpdelpair;
	while(!feof(f_del))
	{
		if(ch==-1)
		{
			break;
		}
		if(ch==' ')
		{
			tmpdelpair.readname1=str.c_str();
			str.clear();
		}
		else if(ch=='\n')
		{
			tmpdelpair.readname2=str.c_str();
			str.clear();
			delpairlist.push_back(tmpdelpair);
		}
		else
		{
			str+=ch;
		}
		ch=fgetc(f_del);
	}
}

void deleteedge()
{
	for(int i=0;i<orim4list.size();i++)
	{
		if(i%100==0)
			{
				//cout<<"i "<<i<<"of "<<orim4list.size()<<endl;
			}
		for(int j=0;j<delpairlist.size();j++)
		{
			
			if((orim4list[i].readname1.compare(delpairlist[j].readname1)==0&&orim4list[i].readname2.compare(delpairlist[j].readname2)==0)||(orim4list[i].readname1.compare(delpairlist[j].readname2)==0&&orim4list[i].readname2.compare(delpairlist[j].readname1)==0))
			{
				orim4list[i].readname1="";
				orim4list[i].readname2="";
			}
		}
	}
}

void addedge()
{
	/*
	for(int i=0;i<alilist.size();i++)
	{
		for(int j=0;j<orim4list.size();j++)
		{
			if((orim4list[i].readname1.compare(delpairlist[j].readname1)==0&&orim4list[i].readname2.compare(delpairlist[j].readname2)==0)||(orim4list[i].readname1.compare(delpairlist[j].readname2)==0&&orim4list[i].readname2.compare(delpairlist[j].readname1)==0))
			{

			}
		}
	}
	*/
	for(int i=0;i<alilist.size();i++)
	{
		orim4list.push_back(alilist[i]);
	}
}
ofstream fout;
void writenewm4()
{
	for(int i=0;i<orim4list.size();i++)
	{
		if(orim4list[i].readname1.compare("")!=0)
		{
			fout<<orim4list[i].readname1.c_str()<<" "<<orim4list[i].readname2.c_str()<<" "<<orim4list[i].info3.c_str()<<" "<<orim4list[i].info4.c_str()<<" "<<orim4list[i].info5.c_str()<<" "<<orim4list[i].start1<<" "<<orim4list[i].end1<<" "<<orim4list[i].info8.c_str()<<" "<<orim4list[i].info9.c_str()<<" "<<orim4list[i].start2<<" "<<orim4list[i].end2<<" "<<orim4list[i].info12.c_str()<<" "<<orim4list[i].info13.c_str()<<endl;
		}
	}
}

int main(int argc,char* argv[])
{

	string m4file="";
	m4file=argv[1];
	const char* filename1;
	filename1=m4file.c_str();
	f_orim4=fopen(filename1,"r");
	
	
	
	
	
	string delreadsfile="";
	delreadsfile=argv[2];
	const char* filename2;
	filename2=delreadsfile.c_str();
	f_del=fopen(filename2,"r");
	
	readdelfile();
	cout<<"readdelfile();"<<endl;
	readorim4file();
	cout<<"readorim4file();"<<endl;
	deleteedge();
	cout<<"deleteedge();"<<endl;
	string newm4file="";
	newm4file=argv[3];
	const char* filename3;
	filename3=newm4file.c_str();
	
	fout.open(filename3,ios::trunc);
	writenewm4();
	cout<<"writenewm4();"<<endl;
	return 0;
}