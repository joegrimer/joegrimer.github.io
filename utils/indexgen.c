#include <stdio.h> 
#include <dirent.h> 
#include <string.h> 
  
void do_dir(char *path) 
{ 
   struct dirent *de;  // Pointer for directory entry 
   char file_name[1024];

   // opendir() returns a pointer of DIR type.  
   DIR *dr = opendir(path); 

   if (dr == NULL)  // opendir returns NULL if couldn't open directory 
   { 
      printf("Could not open current directory" ); 
      return; 
   } 

   while ((de = readdir(dr)) != NULL) {
      strcpy(file_name, de->d_name);
      if (strcmp(file_name, ".")==0 || strcmp(file_name, "..")==0) continue;
      printf("%s\n", file_name); 
   }
  
   closedir(dr);   
   return; 
} 

int main(void) 
{ 
   do_dir(".");
} 
