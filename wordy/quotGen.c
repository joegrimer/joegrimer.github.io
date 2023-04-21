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

	// first line of the haiku
	short words = 5+semi_rand(5);
	while(words++<5) {
		short adj_no = semi_rand(ADJS);
		printf("%s ",adjs[adj_no]);
	}

	printf("\n");
}

short rand_clock = 0;
int semi_rand(int mod) {
//	rand_clock++;
	unsigned int res = abs(rand()+time(NULL)+(97*rand_clock++))%mod;
	return res;
}
