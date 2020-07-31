from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='DELAY')
    .es('RETRASO')
    .pt('ATRASO')
    .fr(1)
    .ja('ディレイ')
    .ko('딜레이')
    .zhHans('延迟')
    .zhHant('延遲')
    .ar('التأخير الزمني')
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='LEVEL')
    .es('NIVEL')
    .pt('NÍVEL')
    .fr('NIVEAU')
    .ja('レベル')
    .ko('레벨')
    .zhHans('电平')
    .zhHant('電平')
    .ar('المستوَى')
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='PAN OPTIONS')
    .es('OPCIONES DE PANO')
    .pt('OPÇÕES DE PAN')
    .fr('OPTIONS DE PAN')
    .ja('オプション')
    .ko('팬 세부 옵션')
    .zhHans('声像选项')
    .zhHant('聲像選項')
    .ar('خيارات التحريك')
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='PHASE')
    .es('FASE')
    .pt('FASE')
    .fr(1)
    .ja('フェイズ')
    .ko('페이즈')
    .zhHans('相位')
    .zhHant('相位')
    .ar('الطور')
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='PRE PANNING')
    .es('PRE PANO')
    .pt('PRÉ-PAN')
    .fr('PRÉ-PAN')
    .ja('適用前設定')
    .ko('팬 적용전')
    .zhHans('声像前')
    .zhHant('聲像前')
    .ar('قبل التحريك')
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='SPECTRAL')
    .es('ESPECTRAL')
    .pt('ESPECTRAL')
    .fr(1)
    .ja('スペクトラル')
    .ko('스펙트럼')
    .zhHans('光谱')
    .zhHant('光譜')
    .ar('طيفي')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Flip L/R')
    .es('Trocar L/R')
    .pt('Inverter L/R')
    .fr('Inverser L/R')
    .ja('L/R入れ替え')
    .ko('좌/우 뒤집기')
    .zhHans('L/R翻转')
    .zhHant('L/R翻轉')
    .ar(' L/R عَكّس')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Left Polarity')
    .es('Polaridad L')
    .pt('Polaridade – Esq.')
    .fr('Polarité Gauche')
    .ja('左極')
    .ko('좌 채널 극성')
    .zhHans('左声道极性')
    .zhHant('左聲道極性')
    .ar('L قطبية')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Left Trim')
    .es('Ajuste L')
    .pt('Volume – Esquerda')
    .fr('Volume Gauche')
    .ja('左トリム')
    .ko('좌 채널 트림')
    .zhHans('左声道修剪')
    .zhHant('左聲道修剪')
    .ar('L مُوازَنةٌ')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Level Pan Law')
    .es('Ley de panoramización')
    .pt('Lei do Pan')
    .fr('Loi de Panoramique')
    .ja('パンロー')
    .ko('팬 규칙 설정')
    .zhHans('声像定律')
    .zhHant('聲像定律')
    .ar('قانون التحريك')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Level Pan Vol. Comp')
    .es('Compensar vol. de pano.')
    .pt('Compensar Nível de Pan')
    .fr('Compensation de Volume')
    .ja('パンボリューム補償')
    .ko('팬 볼륨 보상')
    .zhHans('电平声像音量补偿')
    .zhHant('電平聲像音量補償')
    .ar('تعويض مستوى صوت التحريك')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Pan Glide Time')
    .es('Barrida de pano.')
    .pt('Tempo de Glide do Pan')
    .fr('Temps de Balayage')
    .ja('パングライドタイム')
    .ko('팬 조절 시간')
    .zhHans('声像滑移时间')
    .zhHant('聲像滑移時間')
    .ar('توقيت انزلاق التحريك')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Right Polarity')
    .es('Polaridad R')
    .pt('Polaridade – Dir.')
    .fr('Polarité Droite')
    .ja('右極')
    .ko('우 채널 극성')
    .zhHans('右声道极性')
    .zhHant('右聲道極性')
    .ar('R قطبية')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Right Trim')
    .es('Ajuste R')
    .pt('Volume – Direita')
    .fr('Volume Droit')
    .ja('右トリム')
    .ko('우 채널 트림')
    .zhHans('右声道修剪')
    .zhHant('右聲道修剪')
    .ar('R مُوازَنةٌ')
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Stereo Width')
    .es('Amplitud estéreo')
    .pt('Abertura do Estéreo')
    .fr('Largeur Stéréo')
    .ja('ステレオ幅')
    .ko('스테레오 폭')
    .zhHans('立体声宽度')
    .zhHant('立體聲寬度')
    .ar(' وُسع إستيريو')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="LeftPolarity",
    text='Inverted')
    .es('Invertido')
    .pt('Invertido')
    .fr('Inversée')
    .ja('逆')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('معكوسة')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="LeftPolarity",
    text='Normal')
    .es(1)
    .pt(1)
    .fr('Normale')
    .ja('普通')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('عادي')
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="LevelPanLaw",
    text='Stereo Balancer')
    .es('Balance estéreo')
    .pt('Equilíbrio do Estéreo')
    .fr('Équilibreur Stéréo')
    .ja('ステレオバランサー')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar('توازن إستيريو')
    .he(0)
)

ts.append(T(tag="Tagline",
    text='New directions in panning.')
    .es('Nuevos horizontes en panoramización.')
    .pt('Novas direções para o pan.')
    .fr('Nouvelles directions de panoramique.')
    .ja('パンニングの革命\u3000次世代Panpot')
    .ko('차세대 패닝')
    .zhHans('声像的新方向')
    .zhHant('聲像的新方向')
    .ar('اتجاهات جديدة في التحريك')
    .he(0)
)

