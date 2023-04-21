#include <stdio.h>
#include <stdlib.h>

int semi_rand(int mod);

#define ADJS 108

main() {
/*
	char subjects[SUBJECTS][20] = {"Life","Gracefullness","Culture","An Ideal","Fate","Thought","Philosophy","A Theory","Corruption","The reader","The writer","That guy over there","Concentration","Tea","Rain","Heat","Exercise"};
*/
	char adjs[ADJS][14] = {
	"black","white","heavy","deadly","potent","feared",
	"musical","merciful","forgotten","chaotic","peaceful","caffinated",
	"cheery","vigilant","dishonourable","airlesss","flying","subterranian",//
	"angry","pacifistic","momentary","eternal","alcoholic","infused",
	"liquid","rusty","good","evil","cloudy","brown",
	"fat","red","blue","yellow","green","saphire",
	"silver","gilden","just","visual","memorable","musical", ////

	"poem","man","sky","puddle","rock","leaf",
	"tree","eye","heart","mind","tortoise","elephant",
	"fire","smoke","tube","truck","pen","clock",
	"cider","keyboard","cube","book","puzzle","box",
	"hat","holiday","weekend","weekday","past","future",
	"riddle","poem","weapon","life","death","memory", ////

	"falling","running","flying","fleeing","living","loving",
	"watching","hearing","thinking","dreaming","firing","returning",
	"going","coming","feeling","thinking","reflecting","devolving",
	"liking","becoming","existing","seeming","implying","showing",
	"fearing","seeking","fencing","reaching","unmaking","obtaining",
//	"","","","","","",//	"","","","","","",
	};
	short adjs_s[ADJS] = {1,1,2,2,2,1,3,3,3,3,2,4,
						2,3,4,2,2,4,2,4,4,3,4,2,
						2,2,1,2,2,1,1,1,1,2,1,2,
						2,2,1,2,3,3,////

						2,1,1,2,1,1,1,1,1,1,1,1,
						1,3,2,2,1,2,1,1,1,1,1,1,
						2,2,2,2,2,2,2,2,2,2,3,3,

						2,2,2,2,3,3,2,3,3,2,3,2,
						2,2,2,2,3,3,2,3,3,2,3,2,
						2,2,2,2,3,3,
						};

	// first line of the haiku
	short syllables = 0;
	while(syllables<5) {
		short adj_no = semi_rand(ADJS);
		if(syllables+adjs_s[adj_no] <=5) {
			syllables+=adjs_s[adj_no];
			printf("%s ",adjs[adj_no]);
		}
		else {
			short i = 0;
			for(i=0;i<ADJS;i++) {
				short alternative=adjs_s[(adj_no+i)%ADJS];
				//printf("%d?,",alternative);
				if(syllables+alternative<=5) {
					syllables+=alternative;
					printf("%s ",adjs[(adj_no+i)%ADJS]);
					break;
				}
			}
			//printf("this should not happen: %d",syllables);
			break;
		}
	}

	printf("\n");

	// second line of the haiku
	syllables = 0;
	while(syllables<7) {
		short adj_no = semi_rand(ADJS);
		if(syllables+adjs_s[adj_no] <=7) {
			syllables+=adjs_s[adj_no];
			printf("%s ",adjs[adj_no]);
		}
		else {
			short i = 0;
			for(i=0;i<ADJS;i++) {
				short alternative=adjs_s[(adj_no+i)%ADJS];
				//printf("%d?,",alternative);
				if(syllables+alternative<=7) {
					syllables+=alternative;
					printf("%s ",adjs[(adj_no+i)%ADJS]);
					break;
				}
			}
			//printf("this should not happen: %d",syllables);
			break;
		}
	}

	printf("\n");

	// third line of the haiku
	syllables = 0;
	while(syllables<5) {
		short adj_no = semi_rand(ADJS);
		if(syllables+adjs_s[adj_no] <=5) {
			syllables+=adjs_s[adj_no];
			printf("%s ",adjs[adj_no]);
		}
		else {
			short i = 0;
			for(i=0;i<ADJS;i++) {
				short alternative=adjs_s[(adj_no+i)%ADJS];
				//printf("%d?,",alternative);
				if(syllables+alternative<=5) {
					syllables+=alternative;
					printf("%s ",adjs[(adj_no+i)%ADJS]);
					break;
				}
			}
			//printf("this should not happen: %d",syllables);
			break;
		}
	}

	printf("\n");
/*	printf("%s %s %s %s\n",
		subjects[semi_rand(SUBJECTS)],
//		parts[semi_rand(PARTS)],
		verbs[semi_rand(VERBS)],
		adjectives[semi_rand(ADJECTIVES)],
		things[semi_rand(THINGS)]
	);
	printf("\n\nNow the rain doth fall\n");
	printf("A fat man falls from the sky\n");
	printf("Just another splash\n");*/
}

short rand_clock = 0;
int semi_rand(int mod) {
//	rand_clock++;
	unsigned int res = abs(rand()+time(NULL)+(97*rand_clock++))%mod;
	return res;
}
