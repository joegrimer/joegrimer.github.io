#include <stdio.h>
#include <math.h>

#define MAX 100
// need to try for 100

double seq[MAX*MAX];
int count = 0;

int check_and_add(int new_int) {
	int i=-1;
		for(i=0;i<MAX*MAX;i++) {
				if(seq[i]==0) break; // reached end of sequence
						else if (seq[i] == new_int) return 1;
							}
								seq[i] = new_int;
									count += 1;
										return 1;
										}

										int main() {

											for (int i=0;i<(MAX*MAX);i++) seq[i] = 0;
												printf("start\n");
													for (int a=2;a<=MAX;a++) for(int b=2;b<=MAX;b++) {
															double new_num = pow(a,b);
																	printf("%lf, ", new_num);
																			check_and_add(new_num);
																				}
																					printf("\ncount: %d\n", count);
																						printf("\nend\n");
																						}
																						