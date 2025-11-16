#include <O2Profiler/Profiler.h>
#include <cstdlib>
#include <vector>

int main() {

	PROFILED("PROFILED test",
		int n = 100000;
		int j = rand() % 100 + n - 100;
		for (int i = 0; i < n; i++) {
			if (i == j) {
				break;
			}
		}
	);

	PROFILE_BEGIN("PROFILE_BEGIN/END test", _some_unique_identifier);
	n = 10000;
	std::vector<int> nums(n);
	int amount = rand() % 100 + n - 100;
	std::vector<int> numsCopy;
	for (int i = 0; i < amount; i++) {
		numsCopy.push_back(nums[i]);
	}
	PROFILE_END(_some_unique_identifier);

	{
		PROFILE_SCOPE("PROFILE_SCOPE test");
		int num = rand() % 100 - 100 + 100000;
		int count = 0;
		for (int i = 2; i < num; i++) {
			if (num % i == 0) {
				count++;
			}
		}
	}

	PROFILE_REPORT();

	return 0;
}