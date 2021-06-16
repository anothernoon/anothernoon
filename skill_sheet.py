#!/usr/bin/env python
# -*- coding:utf-8 -*-


def skill_sheet():
    skill_sheet_dict = {'Abandon_Arc_Rare_Up': '遗留神機品质↑',
                        'Abandoned_Arc_Parts_Up': '遗留神機获得率↑',
                        'Acrobat_Team': '特技',
                        'Additional_GAP': 'ＧＡＰ追加取得',
                        'Adrenaline_Rush': '肾上腺素爆发',
                        'Aid_Burst': '使援助对象爆裂',
                        'Aid_Recovery_Amount': '救命回復量',
                        'All_Out_Attack': '全力攻撃',
                        'Ammo_Master': '弹药大师',
                        'Athlete': '运动员',
                        'Attack_Boost': '攻撃力上昇',
                        'Attack_Down': '攻撃力下降',
                        'Attack_Up_on_Aid': '治疗時攻撃ＵＰ',
                        'Attack_Up_on_Rescue': '被治疗時攻撃ＵＰ',
                        'Auto_Aim': '自动瞄准',
                        'Auto_Guard': '自动防御',
                        'Beloved': '親愛',
                        'Bind': '封神',
                        'Bomb_Master': '炸弹大师',
                        'Bond_Break_Reward_Up': '結合崩壊報酬追加',
                        'Burst_Duration': '爆裂时间',
                        'Calm_Breather': '屏息',
                        'Charged_Ability_Speed': '冲刺動作速度',
                        'Charisma': '魅力',
                        'Close_Quarters_ATK': '近距离攻击力',
                        'Close_Quarters_DEF': '近距离防御力',
                        'Combo_Master_B': '连击大师B',
                        'Connoisseur': '鉴定',
                        'Conserve_Stamina': '耐力消費量減少',
                        'Covert_Team': '隠密集団',
                        'Crush_Up': '破碎属性赋予',
                        'Damage_Cut': '伤害削减',
                        'Debuff_Stacking': '状態異常蓄積',
                        'Debuff_Stacking_B': '状態異常蓄積B',
                        'Defense_Up_on_Aid': '治疗時防御ＵＰ',
                        'Defense_Up_on_Rescue': '被治疗時防御ＵＰ',
                        'Devour_Bullet_Power': '捕食获得弹药威力',
                        'Devour_Bullet_Qty_B': '捕喰時獲得弾数B',
                        'Devour_HP_Absorb': '捕食时吸收HP',
                        'Devour_Intake': '捕喰吸収量',
                        'Dexterous': '灵巧',
                        'Disable_Homing': '禁用导航',
                        'Disguise_Scent': '偽装信息素',
                        'Drama_Queen': '夸张',
                        'Effect_Duration': '效果持续时间',
                        'Endurance_Recovery': '耐久値回復',
                        'Enemy_Calm': '敵活性化抑制',
                        'Enemy_Focus_B': '超消音B',
                        'Enemy_HP_Vision': '敵体力視覚化',
                        'Enemy_HP_Vision_B': '敵体力視覚化B',
                        'Exterminator': '驱除效果',
                        'Firm_Stand': '坚定的意志',
                        'Firm_Stand_B': '坚定的意志B',
                        'Friendship': '友情',
                        'Get_Consumable_Items': '消耗品获得率↑',
                        'Giving': '奉献精神',
                        'God_of_Rare_Drops': '稀有物品获得率下降',
                        'Greedy': '贪婪',
                        'Guard_Radius': '防御范围',
                        'Guard_Speed': '防御速度',
                        'Guard_Stamina_B': '防御消耗的耐力B',
                        'Gun_ATK': '枪攻击力',
                        'Gun_ATK_B': '銃攻撃力B',
                        'Gun_Focus_Specialist': '枪特殊行动抑制无效',
                        'Gun_Form_Lock_On': '枪形态锁定',
                        'Gun_Speed_Specialist': '枪特殊行动速度',
                        'HP_Recovery_B': 'HP自動回復B',
                        'Hate_Control_B': '仇恨低下抑制B',
                        'Hate_Up': '吸引荒神注意力',
                        'Hate_Up_B': '仇恨上昇量B',
                        'Heal_Bullet_OP_Use_B': '回復弾ＯＰ消費量B',
                        'Health': '体力',
                        'Hidden_Attack': '隐秘攻击',
                        'Hold': '持有',
                        'Ignore_Bond': '条件無視：結合崩壊',
                        'Ignore_Endurance': '条件無視：耐久値',
                        'Ignore_Time': '条件無視：清楚時間',
                        'Individual_AP_Up': '個人取得ＡＰ↑',
                        'Item_Effect_B': '道具効果B',
                        'Item_Effect_Duration_B': '道具持续时间B',
                        'Item_Effects': '道具效果',
                        'Item_Speed': '道具使用速度',
                        'Item_Speed_B': '道具使用速度B',
                        'JG_HP_Restore': 'ＪＧＨＰ回復',
                        'JG_OP_Restore': 'ＪＧＯＰ回復',
                        'JG_Stamina_Restore': 'ＪＧＳＴ回復',
                        'Jamming': '干扰',
                        'Jamming_Resistance': '干扰抗性',
                        'Knockback': '击退距离',
                        'Laser_Master': '激光大师',
                        'Leak_Resistance': '雷抗性',
                        'Link_Aid_Efficiency_B': '链接援助効率B',
                        'Lucky': '大吉',
                        'Melee_ATK': '近战攻击力',
                        'Melee_ATK_B': '近接攻撃力B',
                        'Melee_ATK_HP_Absorb_B': '近战攻撃体力吸収B',
                        'Melee_Atk_Specialist': '近战特殊攻撃威力',
                        'Melee_Attack_Speed': '近战攻速',
                        'Melee_SPCL_ATK_Stam': '近战特殊攻撃ＳＴ',
                        'Mid_Air_Jump': '空中跳跃',
                        'Mid_Air_Melee_ATK_B': '空中近接攻撃力B',
                        'Muted': '消音',
                        'Mutual_Burst': '援助时双方同时爆裂',
                        'OP_Recovery_B': 'OP自動回復B',
                        'Oracle_Absorption': 'OP吸收量',
                        'Oracle_Absorption_B': 'OP吸収量B',
                        'Prepared': '覚悟',
                        'Prepared_B': '覚悟B',
                        'Pyro_Master': '火焰大师',
                        'Rare_Items_for_All': '全员稀有物品获得率上升',
                        'Recovery_Item_Speed_B': '回收物品的速度B',
                        'Recovery_Up_on_Aid': '治疗時回復量上昇',
                        'Recovery_Up_on_Rescue': '被治疗時回復量上昇',
                        'Reduced_Guard_Damage': '减少防御时收到的伤害',
                        'Reduced_Guard_Damage_B': '减少防御伤害时损失的HPB',
                        'Resilience': '耐久値減少防止',
                        'Reward_Credits_Up': '報酬金額↑',
                        'Reward_Rate_Up': '報酬確率↑',
                        'Sensitive': '敏捷',
                        'Sensitive_B': '敏捷的B',
                        'Share_the_Wealth': '全员物品回收',
                        'Speed': '移動速度',
                        'Speed_Up_on_Aid': '治疗時移動速度上昇',
                        'Stamina': '耐力',
                        'Stamina_Auto_Recovery': '耐力自动回复',
                        'Stamina_Auto_Recovery_B': '耐力自動回復B',
                        'Step_Distance': '移动距离',
                        'Steps_Master': '冲刺大师',
                        'Stun_Resistance': '眩晕抗性',
                        'Sunder_Up': '切断属性赋予',
                        'Support_Redraw': '支援効果再抽選',
                        'Support_Skill_Uses_1': '支援効果発動＋１',
                        'Support_Skills': '支援技能发动',
                        'Survival_Instinct': '生存本能',
                        'Team_AP_Up': '全体取得ＡＰ↑',
                        'Total_Debuff_Resist_B': '全状態異常耐性B',
                        'Total_Endurance_Up': '耐久値上限',
                        'Trigger_Happy': '好战的',
                        'Venom': '雷属性攻击',
                        'Venom_Resistance': '毒抗性',
                        'Wild_Instinct': '生存本能全開',
                        'Wrath_of_Revenge': '愤怒的复仇'
                        }
    return skill_sheet_dict
