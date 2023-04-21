#include <stdio.h>
#include <stdlib.h>

int semi_rand(int mod);

#define SUBJECTS 17
#define VERBS 13
#define ADJECTIVES 24
#define THINGS 24

main() {

	char subjects[SUBJECTS][20] = {"Life","Gracefullness","Culture","An Ideal","Fate","Thought","Philosophy","A Theory","Corruption","The reader","The writer","That guy over there","Concentration","Tea","Rain","Heat","Exercise"};
	char verbs[VERBS][24] = {"is like a","will become the","was once the","seems to me like","implies a","shows the","fears to be the","seeks the","lives for","seeks","fears","reaches","found the"};
	char adjectives[ADJECTIVES][14] = {"black","white","heavy","deadly","potent","feared","musical","merciful","forgotten","chaotic","peaceful","caffinated","cheery","vigilant","dishonourable","airlesss","flying","subterranian","angry","pacifistic","momentary","eternal","alcoholic","infused"};
	char things[THINGS][10] = {"tortoise","elephant","fire","smoke","tube","truck","pen","clock","cider","keyboard","cube","book","puzzle","box","hat","holiday","weekend","weekday","past","future","riddle","poem","weapon","life"};

	printf("%s %s %s %s\n",
		subjects[semi_rand(SUBJECTS)],
//		parts[semi_rand(PARTS)],
		verbs[semi_rand(VERBS)],
		adjectives[semi_rand(ADJECTIVES)],
		things[semi_rand(THINGS)]
	);
}

int semi_rand(int mod) {
	unsigned int res = abs(rand()+time(NULL)+97)%mod;
	//printf("(%d,%d,%d,%d=%d)",mod,rand(),time(),time(NULL),res);
	return res;//(rand()+time(NULL)+97)%mod;
}
