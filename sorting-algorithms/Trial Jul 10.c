#include<stdio.h>
#include<stdlib.h>
#include<inttypes.h>
int64_t inv=0; //Counts inversions
void Merge(int a[], int n, int b[], int m, int* c){

    int i=0, j=0, ctr=0;
    while(ctr<(n+m)){
        if(i<n&&j<m){
            if(a[i]<=b[j]){
                c[ctr]=a[i];
                ctr++;
                i++;
            }
            else{
                c[ctr]=b[j];
                ctr++;
                j++;
                inv+=(n-i);
            }
        }
        else if(i==n&&j==m){
            break;
        }
        else if(i==n&&j<m){
            c[ctr]=b[j];
            j++;
            ctr++;
        }else if(j==m&&i<n){
            c[ctr]=a[i];
            i++;
            ctr++;
        }
    }
}
void Sort(int a[], int n, int* b){
    int *c, *d, *e;
    if(n==1){
        *b =*a;
    }else{
        int cn = n-(n/2), dn=n/2;  //decides the sizes of the smaller arrays.
        c = (int*)(malloc((sizeof(int)*cn)));
        d = (int*)(malloc((sizeof(int)*dn)));
        e = (int*)(malloc((sizeof(int)*(cn+dn))));
        Sort(a,cn,c);
        Sort(a+cn,dn,d);
        Merge(c,cn,d,dn,b);
    }
}
void main(){
        //int a[]={6,5,4,3,2,1};FILE *fp;
        int i = 0;
        int a[100000];
        FILE *fp = fopen("IntegerArray123.txt","r");
        for(i=0;i<100000;i++){
            fscanf(fp,"%u",&a[i]);
        }
        fclose(fp);
        int n = sizeof(a)/sizeof(int);
        int* c = (int*)(malloc((sizeof(a))));
        Sort(a,n,c);
        for(i=0;i<n;i++){
            printf("%d,", *(c+i));
        }
        printf("%u", inv);
}
