#include <stdio.h>

int strlen(char *s);

int main()
{
   char *sample = "cow man wake up";
   char *regex = "cow man ...e up";

   printf("samele string: %s\n", sample);
   printf("regex: %s\n", regex);

   int sample_len = strlen(sample);
   printf("string len: %d\n", sample_len);

   int i;
   for(i=0;i<sample_len;i++) {
      char sample_letter = sample[i];
      char regex_letter = regex[i];

      printf("sample regex: %d %d\n", sample_letter, regex_letter);
      if(regex_letter == '.') continue;
      else if(sample_letter != regex_letter) return 1;
   }

   return 0;
}

int strlen(char *s)
{
   int n;
   for (n=0;*s != '\0' ; s++)
   n++;
   return n;
}

