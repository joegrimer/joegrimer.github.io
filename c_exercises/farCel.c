#include <stdio.h>

/* print Fahrenheit-Celsius table
    for fahr = 0, 20, ..., 300 */
main() {
	float fahr, celsius;
	int lower, upper, step;

	lower = 0; /*lower limit of temperature table*/
	upper = 300; /*upper limit*/
	step = 30; /* step size*/

	printf("This is a simple program which prints a fahrenheit celsius table\n\n");

	fahr = lower;
	while (fahr <= upper) {
		celsius = (5.0/9.0) * (fahr-32.0);
		printf("%3.0f %6.1f\n", fahr, celsius);
		fahr = fahr + step;
	}

	fahr = lower;
	while (fahr <= upper) {
		celsius = (5.0/9.0) * (fahr-32.0);
		printf("%3.0f %6.1f\n", celsius, fahr);
		fahr = fahr + step;
	}
}
