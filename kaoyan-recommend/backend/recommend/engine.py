import logging

logger = logging.getLogger('recommend')

class RuleRecommendEngine:
    """规则推荐引擎（非AI降级方案）"""

    def score_university(self, profile, university, major, admission):
        score = 0
        reasons = []
        risks = []

        # 层次匹配
        if university.level == '985':
            score += 30
            reasons.append('院校层次为985')
        elif university.level == '211':
            score += 20
            reasons.append('院校层次为211')
        else:
            score += 10
            reasons.append('院校层次为双非')

        # 地域匹配
        if profile.preferred_region and profile.preferred_region in university.region:
            score += 25
            reasons.append(f'地域符合意向（{university.region}）')

        # 分数匹配度
        try:
            rank = int(''.join(filter(str.isdigit, profile.rank_percent.split('%')[0])))
        except Exception:
            rank = 50
        if rank <= 20:
            score += 30
            reasons.append('成绩排名靠前，匹配度较高')
        elif rank <= 50:
            score += 20
            reasons.append('成绩排名中等，匹配度适中')
        else:
            score += 10
            risks.append('成绩排名偏后，冲刺风险较高')

        # 报录比处理（实验3要求：缺失不杜撰）
        if admission.pending or not admission.ratio:
            risks.append('报录比待核实，请以官网为准')
        else:
            reasons.append(f'报录比{admission.ratio}')

        return score, '；'.join(reasons), '；'.join(risks)

    def recommend(self, profile, candidates):
        results = []
        for university, major, admission in candidates:
            score, reason, risk = self.score_university(profile, university, major, admission)
            results.append({
                'university': university.name,
                'major': major.name,
                'score_line': admission.score_line,
                'ratio': admission.ratio or '待核实',
                'reason': reason,
                'risk': risk,
                'pending': admission.pending,
                '_score': score,
            })
        results.sort(key=lambda x: x['_score'], reverse=True)
        return results