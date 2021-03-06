# -*- coding:utf-8 -*-

import discord, asyncio

token = "ODE3NDY0NzY0NTgxNDEyOTQ0.YEJ5Yw.qDq5w4IJCpl5EuMMEoS14pWaV3w"
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("레식홍보"))
    print("봇 작동중!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
      return None

    if message.content == "%명령어":
        embed = discord.Embed(title="명령어 목록", description="레.식.좋.아", color=0x62c1cc)
        
        embed.add_field(name="부착물설명", value="%부착물", inline=True)
        embed.add_field(name="반동잡기", value="%반동" , inline=True)
        embed.add_field(name="부착물목록", value="%부착물목록", inline=False)
        embed.add_field(name="오퍼설명", value="%오퍼이름", inline=True)
        embed.add_field(name="맵", value="%맵이름", inline=True)
        embed.add_field(name="오퍼이름", value="%오퍼목록", inline=False)
        embed.add_field(name="레식 유튜버", value="%레식유튜브", inline=True)
        embed.add_field(name="레식구매", value="%레식구매", inline=True)

        await message.channel.send(embed=embed)

    if message.content == "%부착물":
        await message.channel.send("%부착물이름치면 설명나옴")

    if message.content == "%소음기":
        await message.channel.send("데미지15%감소, 위협표시X")
    if message.content == "%소염기":
        await message.channel.send("초탄반동 37.5%감소, 반동회복시간30%감소, 좌우반동5%감소")
    if message.content == "%보정기":    
        await message.channel.send("좌우반동17.75%감소")
    if message.content == "%포구":
        await message.channel.send("초탄반동45%감소, 반동회복시간45%감소")
    if message.content == "%연장":
        await message.channel.send("원거리 데미지 15~20%증가")
    if message.content == "%수직":
        await message.channel.send("수직반동 잘잡아줌(원거리전)")
    if message.content == "%각진":
        await message.channel.send("조준속도 40%감소(근거리전)")
    if message.content == "%레이저":
        await message.channel.send("지향사격범위 감소")
    
    if message.content == "%부착물목록":
        await message.channel.send("소음기, 소염기, 보정기, 포구, 연장, 수직, 각진, 레이저")

    if message.content == "%반동":
        await message.channel.send("https://www.youtube.com/watch?v=jQqdWsvBteA&list=PL7XpKvPYWX3D-2OQ6Ci87TFyQtEX52wCd&index=3&t=3s")

    if message.content == "%오퍼목록":
        embed = discord.Embed(title="오퍼목록", description="오퍼한글")
        
        embed.add_field(name="공격팀 3속도 1장갑", value="애쉬, 아이큐, 카피탕, 히바나, 매버릭", inline=False)
        embed.add_field(name="공격팀 2속도 2장갑", value="슬렛지, 대처, 써마이트, 트위치, 글라즈, 블리츠, 벅, 블비, 자칼, 잉, 조피아, 도깨비, 라이언, 핀카, 노마드, 뇌크, 아마루, 칼리, 이아나, 에이스, 제로", inline=False)
        embed.add_field(name="공격팀 1속도 3장갑", value="몽타뉴, 퓨즈, 그리드락", inline=False)
        embed.add_field(name="방어팀 3속도 1장갑", value="펄스, 밴딧, 카베이라, 엘라, 비질, 알리바이, 멜루시", inline=False)
        embed.add_field(name="방어팀 2속도 2장갑", value="스모커, 뮤트, 캐슬, 캅칸, 예거, 프로스트, 리전, 모찌, 워든, 고요, 와마이, 오닉스, 아루니", inline=False)
        embed.add_field(name="방어팀 1속도 3장갑", value="룩, 닥, 타찬카, 에코, 미라, 마에스트로, 클래쉬, 카이드", inline=False)

        await message.channel.send(embed=embed)

    if message.content == "%애쉬":
        embed = discord.Embed(title="능력-파쇄탄(3발)", description="방어팀 가젯을 파괴하는 원거리탄을 쏜다. 파쇄탄 자체 폭파딜은 50이다. 사실 애쉬의 진짜 능력은 빠른 속도와 좋은 총이다.")
        await message.channel.send(embed=embed)
    if message.content == "%아이큐":
        embed = discord.Embed(title="능력-탐지", description="방어팀의 전자가젯을 찾아낸다.(폭탄, 뮤트재머, 발키리캠, 카이드전기집게발, CCTV, 비질능력, 펄스심장박동기, C4, 엘라진탕지뢰, 에코드론, 방어팀휴대폰, 멜루시밴시, 예거ADS, 리전고독, 근접알람 등등)")
        await message.channel.send(embed=embed)
    if message.content == "%카피탕":
        embed = discord.Embed(title="능력-크로스보우", description="원거리에서 쏠수있는 연막(2발), 불화살(2발)이 장전된 크로스보우를 쓴다.")
        await message.channel.send(embed=embed)
    if message.content == "%히바나":
        embed = discord.Embed(title="능력-펠릿(18개)", description="강화된 벽을 뚫을수 있는 펠릿을 발사후 재시전시 작동시킨다. 2개, 4개, 6개로 나눠 쏠수 있으며, 미강화트랩도어(2개), 강화트랩도어(4개)를 소모하여 트랩도어를 열수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%매버릭":
        embed = discord.Embed(title="능력-토치(6개)", description="강화된 벽을 구멍내는 토치를 사용한다. 강화된 벽의 위 아래를 일자로 녹일시 강화만 해제되고 공갈벽만 남길 수 있다. 근접에서 사용하면 방어팀 가젯들을 부술수 있다.")
        await message.channel.send(embed=embed)
    
        await message.channel.send(embed=embed)
    if message.content == "%대처":
        embed = discord.Embed(title="능력-EMP 수류탄(3개)", description="수류탄 범위내의 방어팀의 전자가젯을 15초간 무력화 시킨다.(발키리캠, 에코드론, 마에캠, 모찌드론, CCTV, C4, 스모커가스탄 등등) ")
        await message.channel.send(embed=embed)
    if message.content == "%스모커":
        embed = discord.Embed(title="능력-가스탄(3개)", description="원격으로 폭파가능한 독가스탄을 사용한다. 독가스는 15~25데미지를 입히며 8초동안 지속된다.")
        await message.channel.send(embed=embed)
    if message.content == "%써마이트":
        embed = discord.Embed(title="능력-발열성폭약(2개)", description="강화된벽을 큰 범위로 파괴시키는 폭약을 설치, 폭파시킨다. 폭파 범위가 넓어 트랩도어 옆이더라도 트랩도어가 같이 터진다.")
        await message.channel.send(embed=embed)
    if message.content == "%뮤트":
        embed = discord.Embed(title="능력-재머(4개)", description="일정거리내의 공격팀의 전자장비를 방해한다.(범위내에서 블리츠의 능력이 봉인되고, 도깨비,라이언능력의 영향을 받지 않는다.)")
        await message.channel.send(embed=embed)
    if message.content == "%캐슬":
        embed = discord.Embed(title="능력-방탄패널(3개)", description="바리게이트를 부수고 방탄 패널을 설치한다. 방탄패널은 폭파 또는 기본공격 12회로만 파괴된다.")
        await message.channel.send(embed=embed)
    if message.content == "%펄스":
        embed = discord.Embed(title="능력-심장박동기", description="심장박동기를 사용해 장애물(벽) 뒤의 적을 감지할 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%트위치":
        embed = discord.Embed(title="능력-감전드론(2개)", description="전기충격을 가할수 있는 드론을 사용한다. 단, 감전드론은 점프할 수 없다.")
        await message.channel.send(embed=embed)
    if message.content == "%몽타뉴":
        embed = discord.Embed(title="능력-방패전개", description="자신의 앞을 모두 덮는 방패를 전개한다. 디퓨저 설치 또는 마우스 휠 사용시 방패를 뒤로 맨다.")
        await message.channel.send(embed=embed)
    if message.content == "%닥":
        embed = discord.Embed(title="능력-회복권총(3발)", description="원거리에서 회복을 시킬 수 있는 권총을 사용한다. 자힐이 가능하며, 힐량은 40이다. 다운된 아군에게 적중시 75의 체력으로 회복시킨다.")
        await message.channel.send(embed=embed)
    if message.content == "%룩":
        embed = discord.Embed(title="능력-방탄팩", description="방어력을 20% 증가시켜주는 방탄팩을 설치한다.")
        await message.channel.send(embed=embed)
    if message.content == "%글라즈":
        embed = discord.Embed(title="능력-접이식조준경", description="열화상 배율 조준경을 사용할 수 있다. 정지상태시 연막속을 볼 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%퓨즈":
        embed = discord.Embed(title="능력-초코파이(4개)", description="파괴가능한 벽, 바닥 등을 관통하여 소형 수류탄을 5개 발사하는 집속탄을 사용한다. 설치후 사용 가능하다.")
        await message.channel.send(embed=embed)
    
    if message.content == "%타찬카":
        embed = discord.Embed(title="능력-유탄(10발)", description="카피탕의 불화살과 같이 지속딜을 주는 유탄을 사용한다. 데미지는 틱당 12, 지속시간은 5초다.")
        await message.channel.send(embed=embed)
    if message.content == "%블리츠":
        embed = discord.Embed(title="능력-섬광방패(4회)", description="방패 앞에 섬광장치가 있다. 격발시 전방의 적의 시야를 뺏을 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%예거":
        embed = discord.Embed(title="능력-ADS(3개)", description="투척무기류들을 요격하는 ADS를 설치한다. 요격시 쿨타임 10초 후 재요격한다.")
        await message.channel.send(embed=embed)
    if message.content == "%벅":
        embed = discord.Embed(title="능력-샷건(31발)", description="주무기와 샷건을 교체하며 사용할 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%블비":
        embed = discord.Embed(title="능력-소총방패(2개)", description="머리를 보호하는 방패를 주무기에 장착한다. 방패 내구도 20. 사용시 이동속도 30% 감소.")
        await message.channel.send(embed=embed)
    if message.content == "%프로스트":
        embed = discord.Embed(title="능력-덫(3개)", description="밟으면 부상 당하는 함정을 깐다.")
        await message.channel.send(embed=embed)   
    if message.content == "%발키리":
        embed = discord.Embed(title="능력-캠(3개)", description="투척 가능한 카메라를 던진다.")
        await message.channel.send(embed=embed)
    if message.content == "%자칼":
        embed = discord.Embed(title="능력-추적(3개)", description="적이 남기지 얼마 안된 발자국을 볼 수 있고, 발자국에 능력사용시 발자국이 사라지는 대신 적의 위치가 일정 시간마다 표시된다.")
        await message.channel.send(embed=embed)
    if message.content == "%잉":
        embed = discord.Embed(title="능력-칸델라(3개)", description="차징, 설치하여 쓸수 있는 섬광 집속탄을 던진다. 칸델라 투척시 자신은 섬광탄의 영향을 받지 않는다.")
        await message.channel.send(embed=embed)
    if message.content == "%카베이라":
        embed = discord.Embed(title="능력-심문", description="능력시전시 발소리가 크게 감소하고 이때 적을 사살시 부상상태가 된다. 부상상태의 적에게 심문을 시전할 수 있으며 심문시 남은 모든 적의 위치가 10초간 공개된다.")
        await message.channel.send(embed=embed)
    if message.content == "%에코":
        embed = discord.Embed(title="능력-요괴(2개)", description="요괴 드론을 사용한다. 요괴드론은 천장에 붙을 수 있으며, 부착시 진탕효과를 주는 초음파를 발사 할 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%미라":
        embed = discord.Embed(title="능력-거울(2개)", description="일방적 투과를 하는 거울을 설치한다. 거울은 방탄이며, 반대쪽에서는 검은색만 보인다.")
        await message.channel.send(embed=embed)
    if message.content == "%리전":
        embed = discord.Embed(title="능력-고독(8개)", description="밟으면 일정시간뒤 틱 데미지를 받는 투척용 덫을 사용한다. 덫을 밟으면 뛸 수 없으며 이동속도가 감소된다.")
        await message.channel.send(embed=embed)
    if message.content == "%엘라":
        embed = discord.Embed(title="능력-진탕지뢰(3개)", description="적이 접근시 폭파하며 적을 진탕시키는 투척용 지뢰를 설치한다.")
        await message.channel.send(embed=embed)
    if message.content == "%조피아":
        embed = discord.Embed(title="능력-진탕,파쇄탄(각각2발)", description="진탕탄과 파쇄탄을 쏠 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%도깨비":
        embed = discord.Embed(title="능력-해킹(2회)", description="잠시동안 모든 적의 휴대폰에 진동소리가 나게하고 휴대폰 사용을 정지시킨다. 사망한 적의 휴대폰을 해킹할 수 있으며 해킹시 모든 관측 기기의 시청이 가능하다.")
        await message.channel.send(embed=embed)
    if message.content == "%비질":
        embed = discord.Embed(title="능력-은신", description="능력 사용시 드론에게 일그러진 모양으로 거의 노출되지 않게 된다.")
        await message.channel.send(embed=embed)
    if message.content == "%라이온":
        embed = discord.Embed(title="능력-움직임 감지(3회)", description="카운트 다운후 움직이는 적의 위치를 표시해 준다.")
        await message.channel.send(embed=embed)
    if message.content == "%핀카":
        embed = discord.Embed(title="능력-아드레날린(3회)", description="시전시 모든 아군에게 버프를 건다. [20의 임시체력, 줌속도 25%감소, 반동 50%감소, 장전시간 25%감소, 이동속도 방해효과 25% 저항, 섬광(50%)-진탕(70%)지속시간 감소, 부상당한 아군 소생(프로스트덫 제외)]")
        await message.channel.send(embed=embed)
    if message.content == "%마에스트로":
        embed = discord.Embed(title="능력-악의눈(2개)", description="방탄 카메라를 설치한다. 전기충격을 발사할 수 있지만 전기충격 발사모드시 전면 방탄 기능이 상실된다. 연막속을 볼수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%알리바이":
        embed = discord.Embed(title="능력-홀로그램(3개)", description="자신의 홀로그램 분신을 설치할 수 있다. 홀로그램을 쏘거나 닿은 적은 위치가 일정 시간동안 표시 당한다.")
        await message.channel.send(embed=embed)
    if message.content == "%노마드":
        embed = discord.Embed(title="능력-기압탄(3개)", description="적이 범위에 들어올 시 주변의 것들을 밀쳐내며 넘어뜨리는 기압탄을 발사하여 설치한다. 한번쏜 기압탄은 회수 할 수 없다.")
        await message.channel.send(embed=embed)
    
    if message.content == "%카이드":
        embed = discord.Embed(title="능력-전기집게발(2개)", description="일정 범위내의 철조망, 이동식방패, 강화벽에 전기가 흐르게 할 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%그리드락":
        embed = discord.Embed(title="능력-트랙스(3개)", description="적이 밟으면 느려지고 데미지를 받는 덫들을 투척한다.")
        await message.channel.send(embed=embed)
    if message.content == "%뇌크":
        embed = discord.Embed(title="능력-은신", description="모든 카메라에게 일그러진 은신을 하며, 이동속도 방해 가젯을 무시한다.(멜루시밴시, 캅칸EDD 등)")
        await message.channel.send(embed=embed)
    if message.content == "%모찌":
        embed = discord.Embed(title="능력-해충(3개)", description="해충을 설치, 발사하여 적의 드론을 해킹하여 사용할 수있다.")
        await message.channel.send(embed=embed)
    if message.content == "%워든":
        embed = discord.Embed(title="능력-스마트안경", description="능력 시전시 섬광의 효과를 무시하고, 연막 내부를 볼 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%아마루":
        embed = discord.Embed(title="능력-후크(4회)", description="능력 사용시 바리게이트, 트랩도어, 옥상 등을 빠르게 올라갈 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%칼리":
        embed = discord.Embed(title="능력-집게 파쇄탄(3개)", description="벽뒤의 가젯을 파괴시키는 파쇄탄을 발사 할 수있다.")
        await message.channel.send(embed=embed)
    if message.content == "%고요":
        embed = discord.Embed(title="능력-발칸방패(2개)", description="뒤의 발칸을 쏘거나 방패 파괴시 카피탕의 불화살 효과를 남기는 방패를 설치할 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%와마이":
        embed = discord.Embed(title="능력-마그넷(4개)", description="적의 투척물들을 빨아들여 자폭하는 가젯을 투척하여 설치할 수있다.")
        await message.channel.send(embed=embed)
    if message.content == "%이아나":
        embed = discord.Embed(title="능력-분신", description="자신의 홀로그램을 한 드론을 사용할 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%에이스":
        embed = discord.Embed(title="능력-셀마(3개)", description="투척시 잠시후 강화된 벽을 파괴하며 한칸 밑으로 1회 전이 된다.")
        await message.channel.send(embed=embed)
    if message.content == "%오릭스":
        embed = discord.Embed(title="능력-돌진", description="능력사용시 앞으로 질주 하며, 강화되지 않은 벽을 파괴한다.")
        await message.channel.send(embed=embed)
    if message.content == "%멜루시":
        embed = discord.Embed(title="능력-밴시(3개)", description="일정 범위내의 적을 느리게 만드는 밴시를 설치 한다.")
        await message.channel.send(embed=embed)
    if message.content == "%제로":
        embed = discord.Embed(title="능력-카메라(4개)", description="카메라를 발사하여, 강화벽내부, 벽등에 부착 시킨다. 부착된 카메라는 전기 충격을 1회 쏠 수 있다.")
        await message.channel.send(embed=embed)
    if message.content == "%아루니":
        embed = discord.Embed(title="능력-게이트()3개", description="벽, 출입구에 게이트를 설치한다. 게이트는 투척무기를 1회 막거나, 적이 통과시 30데미지를 주고 비활성화 된다. 비활성화된 게이트는 30초 뒤에 아군이 총으로 다시 활성화 시킬 수 있다.")
        await message.channel.send(embed=embed)

    if message.content == "%레식유튜브":
        embed = discord.Embed(title="레식유튜버", description="레-식")
        embed.add_field(name="유뚱", value="https://www.youtube.com/channel/UCRBRpCsghvPxWTSUcvhD-Tw", inline=False)
        embed.add_field(name="레지나", value="https://www.youtube.com/channel/UCoGlmInGRIRoDg4NjAYv4-Q", inline=False)
        embed.add_field(name="Static", value="https://www.youtube.com/channel/UCGzbwTQ7byCcMerEuisnVgg", inline=False)
        embed.add_field(name="이하린", value="https://www.youtube.com/channel/UCvBjO5wQ3UMuayJ4BPhnvMw", inline=False)
        embed.add_field(name="박재현", value="https://www.youtube.com/channel/UCAZmZIgWLJN2n2sx_FS-PXw", inline=False)
        embed.add_field(name="렘쨩", value="https://www.youtube.com/user/remguri", inline=False)
        embed.add_field(name="동식", value="https://www.youtube.com/channel/UCHWcZvlFnFSCujxb0EQENow", inline=False)
        embed.add_field(name="개새", value="https://www.youtube.com/channel/UCMd-lEaY1qLt3RMExiPigVw", inline=False)
        await message.channel.send(embed=embed)


client.run(token)