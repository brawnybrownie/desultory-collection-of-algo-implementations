#include<stdio.h>
#include<inttypes.h>
int64_t count=0;
void Swap(int* a, int* b){
    int t;
    t = *a;
    *a = *b;
    *b = t;
}
void qSort(int* arr, int n){
    if(n>1){
    int i=0, j=0, k=n-1, pivot=0, arrtemp[n],s;
    for(i=0;i<n;i++){
        if(i!=pivot){
            count++;
            if(arr[pivot]>arr[i])
                arrtemp[j++]=arr[i];
            if(arr[pivot]<arr[i])
                arrtemp[k--]=arr[i];
        }
    }
    arrtemp[j]=arr[pivot];
    for(s=0;s<n;s++)
    printf("%d", arr[s]);
    qSort(arrtemp,j);
    qSort(&arrtemp[j+1],n-1-j);
    for(i=0;i<n;i++){
        arr[i]=arrtemp[i];
    }
    return 0;
    }
    else{
        return 0;
    }
}
void main(){
    int* arr=(int*)(malloc(10*sizeof(int)));
    FILE *fp;
    int n = 10,i;
    fp = fopen("10.txt","r");
    for(i=0;i<n;i++){
        fscanf(fp,"%d",&arr[i]);
    }
    qSort(arr, 10);
    for(i=0;i<n;i++){
       printf("%d", arr[i]);
    }
    printf("%d", count);
}
