from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        f = [[-10**9-7] * n for _ in range(m)]
        ret = -10**9-7
        f[0][0] = 0
        for i in range(m):
            for j in range(n):
                f[i][j] = nums1[i]*nums2[j]
                if i > 0 and j > 0:
                    f[i][j] = max(f[i][j], f[i-1][j-1] + nums1[i]*nums2[j], f[i-1][j], f[i][j-1])
                elif i > 0:
                    f[i][j] = max(f[i][j], f[i-1][j])
                elif j > 0:
                    f[i][j] = max(f[i][j], f[i][j-1])

        return f[m-1][n-1]




if __name__ == '__main__':
    sol = Solution()
    s = sol.maxDotProduct([-868,-299,-538,-159,-954,887,-964,16,167,384,-637,-521,-51,371,-371,592,-804,433,-244,223,109,110,-440,-334,-269,-691,383,-842,759,-70,280,582,-155,-79,202,537,535,-91,9,206,618,281,781,-954,-351,273,293,-526,-323,310,715,-938,92,-157,514,-679,620,-672,-800,-545,351,-350,-80,-139,2,206,-487,-484,311,-575,-888,-184,-4,564,-156,-9,952,214,-493,663,809,-724,242,381,413,457,750,-183,-924,-317,-213,-772,-971,-940,34,-840,642,700,797,-152,-919,193,-241,-772,710,-761,355,-644,-613,731,-357,-20,933,799,-606,694,-769,886,8,696,594,-617,879,429,-218,560,-273,485,602,371,-195,-94,-115,210,-928,-947,-246,-668,-432,-652,-978,667,911,-346,986,-898,759,-346,-73,-422,46,-726,-101,636,159,-222,-885,-561,-649,354,1,-530,680,-991,-394,820,-752,177,651,-377,249,-298,-765,-742,338,237,133,-779,-397,369,-9,671,678,-742,699,-83,482,-548,-261,280,367,-306,313,-40,-412,-968,411,-317,373,-29,-262,-317,742,-907,-636,442,693,-683,-324,56,-4,357,-760,311,-615,-34,-808,688,-100,874,-552,191,594,-487,146,745,-256,380,-679,-48,-603,-909,999,749,509,-162,-123,942,-724,262,-502,-776,671,-926,323,323,191,-690,-92,-326,-263,-294,-132,12,-553,-472,-98,356,-289,803,-465,18,328,40,157,474,713,-182,894,-127,475,-560,245,760,-217,151,54,-860,-17,824,707,-600,267,-16,445,427,488,-434,-290,-721,230,519,856,406,-228,689,-398,453,-648,-757,847,203,-326,228,-749,-100,877,319,256,957,-945,-376,304,-311,-737,494,784,-235,-953,787],\
[-877,877,199,190,-609,-520,-734,242,-391,-748,-110,-660,387,-410,4,600,-363,581,547,-595,312,321,-796,281,-969,-1,323,-668,-363,430,-85,228,667,-17,-736,62,616,-477,853,-234,-271,-600,-91,118,-462,-679,-14,300,-312,-187,598,-920,596,-994,-697,-708,507,-565,379,948,-380,839,-436,-582,781,-74,654,-530,311,-379,-733,381,-885,-343,-373,-451,89,-916,282,453,314,-615,43,960,965,-239,-561,491,-992,552,909,80,-754,-959,-5,-341,-560,275,871,-197,230,-458,844,652,839,-920,-562,220,-711,-295,-553,529,-201,428,205,-205,788,13,779,-549,-354,498,-420,707,-890,834,754,-745,749,-690,-810,545,-534,248,-202,-971,-726,-457,712,-675,-907,-852,-786,847,-942,-766,-7,875,370,383,-921,234,-731,248,917,-833,726,-59,856,34,-720,728,-889,876,421,-808,572,-648,-763,-778,673,-835,-178,905,-898,-84,-603,278,-663,-693,127,-113,368,-723,351,747,-922,-227,-14,205,270,527,379,-14,600,-893,523,-592,-508,-327,-139,316,-433,668,-614,970,86,-446,767,-594,610,235,968,-866,-126,659,152,-63,652,-170,-159,-457,-987,833,-573,-918,509,-836,341,-324,-665,-610,156,971,604,909,-262,-676,240,-142,-4,-899,-131,-535,989,-410,145,-19,-965,906,774,-349,672,-776,596,468,-973,-161,-680,-380,-114,421,348,555,-935,-329,-21,-765,-822,-329,197,885,-907,-78,748,-567,-957,-358,994,-713,-546,-116,690,999,814,226,764,-463,-718,536,125,-622,-792,230,-883,-601,969,-741,-676,330,-146,-778,808,869,-697,924,614,-565,-244,300,554,546,-880,9,-470,-875,-433,-117,-396,-176,-726,286,281,-284])
    print(s)
    s = sol.maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7])
    print(s)
    s = sol.maxDotProduct(nums1 = [-1,-1], nums2 = [1,1])
    print(s)