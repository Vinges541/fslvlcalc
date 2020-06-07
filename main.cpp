#include <iostream>
int main()
{
	size_t curr_lvl, des_lvl;
	std::cout << "Enter current level: ";
	std::cin >> curr_lvl;
	std::cout << "Enter desired level: ";
	std::cin >> des_lvl;
	if (curr_lvl < 1)
	{
		std::cout << "Wrong current level!" << std::endl;
		return -1;
	}
	size_t needed_souls = 0;
	++curr_lvl;
	for (; curr_lvl <= des_lvl; ++curr_lvl)
	{
		double c = curr_lvl;
		double b = curr_lvl * curr_lvl;
		double a = b * curr_lvl;
		if (curr_lvl >= 12)
		{
			a *= 0.02;
			b *= 3.06;
			c *= 105.6;
			needed_souls += static_cast<size_t>(round(a + b + c)) - 895;
		}
		else if (curr_lvl >= 1 && curr_lvl < 12)
		{
			a *= 0.0068;
			b *= 0.06;
			c *= 17.1;
			needed_souls += static_cast<size_t>(round(a + b + c)) + 639;
		}
	}
	std::cout << "You need " << needed_souls << " souls." << std::endl;
	system("pause");
	return 0;
}