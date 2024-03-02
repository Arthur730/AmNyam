class HSRmath:
    def MainDamage(self, SkillMultiplier, Add_SkillMultiplier, ScalableCharacteristic, Add_Damage):
        return (SkillMultiplier+Add_SkillMultiplier)*ScalableCharacteristic+Add_Damage

    def DamageMultiplier(self, ElementalDamageBonus, DamageBonus, PeriodicDamageBonus):
        return 1+ElementalDamageBonus+DamageBonus+PeriodicDamageBonus

    def ProtectionMultiplier(self, opponentLvl, LoweringProtection, IgnoreProtection, HeroLvl):
        return 1-((opponentLvl+20)/((opponentLvl+20)*(1-LoweringProtection-IgnoreProtection) + HeroLvl +20))

    def ResistanceMultiplier(self, EnemyResistance, LoweringResistance):
        return 1-(EnemyResistance-LoweringResistance)

    def AdditionalDamageMultiplier(self, ElementalDamageBuff, TotalDamageBuff):
        return 1 + ElementalDamageBuff + TotalDamageBuff

    def BreakdownMultiplier(self, bool):
        if bool: return 1
        else: return 0.9

    def CritDamageMultiplier(self, CritDamage):
        return 1+CritDamage