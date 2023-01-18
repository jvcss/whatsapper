import re
from mods import testes 
input_string = """
zero 0⃣
one 1⃣
one-thirty 🕜
o'clock 🕐
two 2⃣
two-thirty 🕝
o'clock 🕑
three 3⃣
three-thirty 🕞
o'clock 🕒
clover 🍀
four-thirty 🕟
o'clock 🕓
four 4⃣
five-thirty 🕠
o'clock 🕔
five 5⃣
number 6⃣
six-thirty 🕡
o'clock 🕕
seven-thirty 🕢
seven 7⃣
o'clock 🕖
8ball 🎱
eight 8⃣
eight-thirty 🕣
o'clock 🕗
nine 9⃣
nine-thirty 🕤
o'clock 🕘
ten-thirty 🕥
o'clock 🕙
eleven-thirty 🕦
o'clock 🕚
twelve-thirty 🕧
o'clock 🕛
eighteen 🔞
store 🏪
definitely 💯
banknote 💶
heart 💙
arrow 💘
yellow 💛
heart 💚
ribbon 💝
heart 💜
decoration 💟
revolving 💞
beating 💓
hearts 💕
heart 💗
heart 💖
eyes 😙
kiss 😘
face 😗
heart-eyes 😍
eyes 😚
numbers 🔢
flick 💁‍♂
hand 💁
finger 🖕
salute 🖖
stop 🖐
lgbtqia 👬
hands 👭
swerve 👐
up 👆
down 👇
right 👉
there? 👋
hand 👌
nice 👍
job 👏
OK 🙆
v ✌
write ✍
hand ✋
fist ✊
fingers 🤟
crossed 🤞
deal 🤝
call 🤙
rock-on 🤘
hand 🙋
praise 🙌
folded 🙏
NO 🙅
gloves 🧤
fist 👊
down 👎
left 👈
this ☝
hand 🙋‍♂
OK 🙆‍♂
NO 🙅‍♂
sos 🆘
i ℹ
done 💅
eyes 🙄
taste 😝
face 😒
impressed 😑
face 😐
yawn 😴
style 🧝‍♀️
elf 🧝‍♂️
woman 👨‍👩‍👧
boy 👩‍👩‍👦‍👦
bisexual 👩‍👩‍👦
bisexual 👩‍👩‍👧
boy 👩‍👦‍👦
man 👨‍👧‍👧
boy 👨‍👧‍👦
bisexual 👨‍👨‍👦
bisexual 👨‍👨‍👧
bisexual 👨‍👨‍👦‍👦
bisexual 👨‍👨‍👧‍👧
bisexual 👨‍👨‍👧‍👦
boy 👨‍👦
man 👨‍👧
boy 👨‍👦‍👦
woman 👩‍👩‍👧‍👧
boy 👩‍👩‍👧‍👦
child 👪
boy 👨‍👩‍👦‍👦
boy 👨‍👩‍👧‍👦
woman 👨‍👩‍👧‍👧
woman 👩‍👧
boy 👩‍👦
boy 👩‍👧‍👦
woman 👩‍👧‍👧
pigtails 👧
person 👱
guapimao 👲
old 👴
helmet 👷
bro 👨
love 👫
officer 👮
shoe 👞
scientist 👨‍🔬
tradesperson 👨‍🔧
firetruck 👨‍🚒
rocket 👨‍🚀
handball 🤾‍♂
white-collar 👨‍💼
tuxedo 🤵
scales 👨‍⚖
therapist 👨‍⚕
technologist 👨‍💻
rancher 👨‍🌾
cook 👨‍🍳
polo 🤽‍♂
gymnastics 🤸‍♂
multitask 🤹‍♂
rockstar 👨‍🎤
artist 👨‍🎨
student 👨‍🎓
pilot 👨‍✈
facepalm 🤦‍♂
room 🚹
teacher 👨‍🏫
industrial 👨‍🏭
suit 🕴
spy 🕵
shrug 🤷‍♂
woman 👵
stilletto 👠
sandal 👡
boot 👢
haircut 👩
white-collar 👩‍💼
hat 👒
clothes 👚
industrial 👩‍🏭
teacher 👩‍🏫
dancing 💃
handball 🤾‍♀
rockstar 👩‍🎤
artist 👩‍🎨
student 👩‍🎓
tradesperson 👩‍🔧
pregnant 🤰
firetruck 👩‍🚒
rocket 👩‍🚀
pilot 👩‍✈
technologist 👩‍💻
facepalm 🤦‍♀
rancher 👩‍🌾
polo 🤽‍♀
gymnastics 🤸‍♀
multitask 🤹‍♀
scales 👩‍⚖
therapist 👩‍⚕
scientist 👩‍🔬
room 🚺
dancing 🕺
blonde 👱‍♀
helmet 👷‍♀
officer 👮‍♀
london 💂‍♀
cook 👩‍🍳
shrug 🤷‍♀
kid 👦
zombie 🧟‍♀️
blood 🧛‍♀️
zombie 🧟‍♂️
Dracula 🧛‍♂️
mask 👹
ghostface 👻
face 😧
mouth 😦
wrapper 🍬
bar 🍫
jack-o-lantern 🎃
square ⬜
square ⬛
button ⏹
square ◼
square ◾
square ▫
square ▪
square ◻
square ◽
button 🔳
button 🔲
inside 💠
circle ⚫
circle ⚪
down 🔻
up 🔺
diamond 🔹
diamond 🔸
diamond 🔷
diamond 🔶
circle 🔵
circle 🔴
button 🔘
Pisces 🐟
spring 🐝
Taurus 🐂
Ophiuchus 🐍
whale 🐳
face 🐲
face 🐱
face 🐰
face 🐷
face 🐶
face 🐵
face 🐴
face 🐻
face 🐺
face 🐹
face 🐸
nose 🐽
face 🐼
chick 🐣
tortoise 🐢
blowfish 🐡
fish 🐠
penguin 🐧
ornithology 🐦
chick 🐥
chick 🐤
camel 🐫
hump 🐪
poodle 🐩
koala 🐨
face 🐯
face 🐮
face 🐭
flipper 🐬
rooster 🐓
monkey 🐒
wool 🐑
Capricorn 🐐
thrones 🐗
sow 🐖
dogs 🐕
chicken 🐔
garden 🐛
shell 🐚
octopus 🐙
elephant 🐘
ladybug 🐞
ant 🐜
buffalo 🐃
mouse 🐁
rat 🐀
rabbit 🐇
zoo 🐅
moo 🐄
whale 🐋
florida 🐊
knights 🐉
cats 🐈
Aries 🐏
equestrian 🐎
snail 🐌
leopard 🐆
monkey 🙈
monkey 🙉
monkey 🙊
face 🙀
heart-eyes 😻
mouth 😺
joy 😹
eyes 😸
face 😿
face 😾
eyes 😽
wry 😼
eagle 🦅
bat 🦇
duck 🦆
lion 🦁
gorilla 🦍
deer 🦌
rhinoceros 🦏
reptile 🦎
owl 🦉
shark 🦈
fox 🦊
squid 🦑
knife 🍴
plate 🍽
swirl 🍥
pole 🎣
horoscope ♓
boat 🚣‍♀
boat 🚣
jug 🏺
Sagittarius 🏹
Libra ⚖
Ophiuchus ⛎
Cancer 🦀
Scorpius 🦂
horoscope ♒
horoscope ♐
horoscope ♑
horoscope ♎
horoscope ♏
horoscope ♌
Virgo ♍
Gemini ♊
horoscope ♋
horoscope ♈
horoscope ♉
pot 🍯
pretty 🦋
Orthoptera 🦗
spider 🕷
drought 🌵
sunrise 🌅
volcano 🌋
wave 🌊
genderqueer 🌈
tear 💧
thunderbolt ⚡
fuji 🗻
blossom 🌸
west ⬅
south ⬇
arrow ⬆
forward ⏩
button ⏪
button ⏫
button ⏬
nexttrack ⏭
track ⏮
button ⏯
button ▶
arrow ➡
arrow 📲
arrow 📩
button 🔽
button 🔼
down ⤵
up ⤴
right ↪
left ↩
intercardinal ↗
arrow ↖
arrow ↕
arrow ↔
southwest ↙
southeast ↘
reverse ◀
withershins 🔄
reload 🔃
once 🔂
button 🔁
button 🔀
arrow 🔝
soon 🔜
on 🔛
arrow 🔚
arrow 🔙
decreasing 📉
Singapore 🇸🇬
Helena 🇸🇭
Slovenia 🇸🇮
Seychelles 🇸🇨
Sudan 🇸🇩
Sweden 🇸🇪
Arabia 🇸🇦
Islands 🇸🇧
Territory 🇮🇴
Maarten 🇸🇽
Syria 🇸🇾
Swaziland 🇸🇿
Sudan 🇸🇸
Príncipe 🇸🇹
Micronesia 🇫🇲
Somalia 🇸🇴
Man 🇮🇲
Suriname 🇸🇷
Slovakia 🇸🇰
Leone 🇸🇱
Marino 🇸🇲
Senegal 🇸🇳
Israel 🇮🇱
Islands 🇫🇴
Fiji 🇫🇯
Italy 🇮🇹
England 🏴󠁧󠁢󠁥󠁮󠁧󠁿
Korea 🇰🇵
Korea 🇰🇷
Comoros 🇰🇲
Kuwait 🇰🇼
Kazakhstan 🇰🇿
Kyrgyzstan 🇰🇬
Kiribati 🇰🇮
Kenya 🇰🇪
Salvador 🇸🇻
Algeria 🇩🇿
Republic 🇩🇴
Denmark 🇩🇰
Dominica 🇩🇲
Djibouti 🇩🇯
Germany 🇩🇪
Ireland 🇮🇪
Islands 🇮🇨
Iran 🇮🇷
India 🇮🇳
Iceland 🇮🇸
Netherlands 🇳🇱
Nauru 🇳🇷
Nepal 🇳🇵
Norway 🇳🇴
Niue 🇳🇺
Zealand 🇳🇿
Namibia 🇳🇦
Island 🇳🇫
Niger 🇳🇪
Caledonia 🇳🇨
Nicaragua 🇳🇮
Nigeria 🇳🇬
Liberia 🇱🇷
Lanka 🇱🇰
Libya 🇱🇾
Lithuania 🇱🇹
Lesotho 🇱🇸
Latvia 🇱🇻
Luxembourg 🇱🇺
Lebanon 🇱🇧
Laos 🇱🇦
Liechtenstein 🇱🇮
Lucia 🇱🇨
Rwanda 🇷🇼
Russia 🇷🇺
Serbia 🇷🇸
Romania 🇷🇴
Réunion 🇷🇪
Mayotte 🇾🇹
Yemen 🇾🇪
Curaçao 🇨🇼
Island 🇨🇽
Cyprus 🇨🇾
Republic 🇨🇿
Cuba 🇨🇺
Verde 🇨🇻
Rica 🇨🇷
Chile 🇨🇱
Cameroon 🇨🇲
China 🇨🇳
Congo 🇨🇬
Switzerland 🇨🇭
d'Ivoire 🇨🇮
Congo 🇨🇩
Republic 🇨🇫
Canada 🇨🇦
Indonesia 🇮🇩
Iraq 🇮🇶
Tanzania 🇹🇿
Tobago 🇹🇹
Islands 🇫🇰
France 🇫🇷
Finland 🇫🇮
Albania 🇦🇱
Tonga 🇹🇴
Venezuela 🇻🇪
Grenadines 🇻🇨
Islands 🇻🇮
Islands 🇻🇬
City 🇻🇦
Vanuatu 🇻🇺
Vietnam 🇻🇳
Morocco 🇲🇦
Montenegro 🇲🇪
Monaco 🇲🇨
Moldova 🇲🇩
Madagascar 🇲🇬
Islands 🇲🇭
Burma 🇲🇲
Mongolia 🇲🇳
Macedonia 🇲🇰
Mali 🇲🇱
Martinique 🇲🇶
Mauritania 🇲🇷
China 🇲🇴
Islands 🇲🇵
Mauritius 🇲🇺
Maldives 🇲🇻
Montserrat 🇲🇸
Malta 🇲🇹
Malaysia 🇲🇾
Mozambique 🇲🇿
Malawi 🇲🇼
Mexico 🇲🇽
flag 🏁
Colombia 🇨🇴
Islands 🇨🇰
Islands 🇨🇨
Nevis 🇰🇳
Islands 🇰🇾
Cambodia 🇰🇭
Panama 🇵🇦
Polynesia 🇵🇫
Peru 🇵🇪
Philippines 🇵🇭
Guinea 🇵🇬
Islands 🇵🇳
Miquelon 🇵🇲
Rico 🇵🇷
Portugal 🇵🇹
Palestine 🇵🇸
Palau 🇵🇼
Paraguay 🇵🇾
Haiti 🇭🇹
Hungary 🇭🇺
China 🇭🇰
Honduras 🇭🇳
Croatia 🇭🇷
Grenada 🇬🇩
Georgia 🇬🇪
Guiana 🇬🇫
Guernsey 🇬🇬
Ghana 🇬🇭
Gibraltar 🇬🇮
Gabon 🇬🇦
uk 🇬🇧
Islands 🇬🇸
Guatemala 🇬🇹
Guam 🇬🇺
Guinea-Bissau 🇬🇼
Guyana 🇬🇾
Greenland 🇬🇱
Gambia 🇬🇲
Guinea 🇬🇳
Guadeloupe 🇬🇵
Guinea 🇬🇶
Greece 🇬🇷
Poland 🇵🇱
Pakistan 🇵🇰
Estonia 🇪🇪
Ecuador 🇪🇨
Egypt 🇪🇬
Sahara 🇪🇭
Union 🇪🇺
Spain 🇪🇸
Ethiopia 🇪🇹
Eritrea 🇪🇷
flag 🚩
Benin 🇧🇯
Burundi 🇧🇮
Bahrain 🇧🇭
Bulgaria 🇧🇬
Faso 🇧🇫
Belgium 🇧🇪
Bangladesh 🇧🇩
Barbados 🇧🇧
Herzegovina 🇧🇦
Belize 🇧🇿
Belarus 🇧🇾
Botswana 🇧🇼
Bhutan 🇧🇹
Bahamas 🇧🇸
Brazil 🇧🇷
Netherlands 🇧🇶
Bolivia 🇧🇴
Brunei 🇧🇳
Bermuda 🇧🇲
Barthélemy 🇧🇱
Tuvalu 🇹🇻
Tokelau 🇹🇰
Tunisia 🇹🇳
Turkmenistan 🇹🇲
Qatar 🇶🇦
Thailand 🇹🇭
Togo 🇹🇬
Tajikistan 🇹🇯
Chad 🇹🇩
Islands 🇹🇨
Territories 🇹🇫
Taiwan 🇹🇼
Turkey 🇹🇷
Timor-Leste 🇹🇱
texas 🇽🇹
scotland 🇽🇸
wales 🇽🇼
Kosovo 🇽🇰
england 🇽🇪
Anguilla 🇦🇮
Barbuda 🇦🇬
Emirates 🇦🇪
Afghanistan 🇦🇫
Andorra 🇦🇩
Azerbaijan 🇦🇿
Aruba 🇦🇼
Islands 🇦🇽
Australia 🇦🇺
Samoa 🇦🇸
Austria 🇦🇹
Antarctica 🇦🇶
Argentina 🇦🇷
Angola 🇦🇴
Armenia 🇦🇲
Samoa 🇼🇸
Futuna 🇼🇫
Jersey 🇯🇪
Japan 🇯🇵
Jordan 🇯🇴
Jamaica 🇯🇲
Wales 🏴󠁧󠁢󠁷󠁬󠁳󠁿
usa 🇺🇸
Uruguay 🇺🇾
Uzbekistan 🇺🇿
Uganda 🇺🇬
Ukraine 🇺🇦
Zambia 🇿🇲
Zimbabwe 🇿🇼
Africa 🇿🇦
Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿
Oman 🇴🇲
hit 🎯
corn 🌽
sign 💲
wings 💸
bag 💰
banknote 💷
teller 🏧
card 💳
banknote 💵
rise 💹
exchange 💱
banknote 💴
stone 💎
face 🤑
building 🏦
score 🎼
note 🎵
notes 🎶
pad 🗒
stink 💩
bubble 💬
smoke 💨
shining 💫
arm 💪
balloon 💭
bulb 💡
explosion 💣
symbol 💢
explode 💥
zzzz 💤
droplets 💦
mean 👺
angel 👼
ufo 👽
monster 👾
demon 👿
eyes 👀
face 🌬
face 🌞
face 🌝
face 🌜
face 🌛
face 🌚
lmao 💀
relaxing 💆
hugging 🤗
robot 🤖
injury 🤕
face 🤔
nerd 🤓
ill 🤒
quiet 🤐
wow 🤩
fever 🤧
liar 🤥
drooling 🤤
laughing 🤣
nasty 🤢
clown 🤡
cowgirl 🤠
face 🙁
face 🙂
upside-down 🙃
tongue 😛
face 😟
face 😞
eye 😜
sweat 😓
annoyed 😖
meh 😕
face 😔
um 😋
eyes 😊
face 😉
horns 😈
face 😏
sunglasses 😎
mouth 😃
joy 😂
eyes 😁
face 😀
halo 😇
sweat 😅
eyes 😄
face 😳
face 😲
munch 😱
sweat 😰
mask 😷
mouth 😶
face 😵
face 😫
face 😪
face 😩
face 😨
face 😯
face 😭
face 😬
face 😣
face 😢
face 😡
face 😠
whew 😥
fume 😤
aid ⛑
face 😌
eyes 😆
unicorn 🦄
sympathy 😮
face ☹
face ☺
massage 💆‍♂
speaking 🗣
moai 🗿
crossbones ☠
celebration 🎈
bubble 🗯
bubble 🗨
moon 🌕
party 👯‍♂
bunny 👯
silhouette 👥
wrestle 🤼‍♂
drink 🍹
hooray 🎉
ball 🎊
running 🏃‍♀
shoe 👟
running 🏃
athletics 🎽
nose 🚅
train 🚄
interrobang ⁉
exclamation ❣
mark ❗
mark ❕
bangbang ‼
mark ❓
mark ❔
tabs 📑
mark ™
part 〽
bookmark 🔖
dash 〰
mahjong 🀄
wildcard 🃏
shuttlecock 🏸
hockey 🏑
game 🎮
playing 🎴
machine 🎰
strike 🎳
die 🎲
stone 🥌
cricket 🏏
puck 🏒
tennis 🏓
volleyball 🏐
suit ♦
suit ♥
suit ♣
suit ♠
videogame 🕹
apple 🍎
rose 🌹
lantern 🏮
keycap *⃣
mouse 🖱
trackball 🖲
desktop 🖥
printer 🖨
keyboard ⌨
personal 💻
optical 💽
disk 💿
disk 💾
dvd 📀
picture 🖼
arts 🎭
palette 🎨
paintbrush 🖌
heart 🖤
heart 💑
mark 💋
letter 💌
anniversary 💏
heart ❤
heart 👩‍❤‍👩
m Ⓜ
o ⭕
button ⏺
octagonal 🛑
stop 🚏
paperclips 🖇
links 🔗
paperclip 📎
crayon 🖍
pen 🖋
fountain ⛲
ballpoint 🖊
privacy 🔏
nib ✒
sign ➖
set 📐
straightedge 📏
sign ➗
sign ➕
star ⭐
star 🌠
stars 🌃
star 🌟
sparkles ✨
David ✡
star ✴
star 🔯
button 🅾
veil 👰
nuptuals 💒
shiny 💍
hat 🎩
scholar 🎓
turban 👳
turban 👳‍♀
adult 🧓
clue 🗝
purse 👜
young 👶
bottle 🍼
feeding 🤱
changing 🚼
sprout 🌱
gender-neutral 🧒
crane 🏗
barrier 🚧
london 💂
queen 👸
family 👑
father 🎅
crystal 🔮
study 📚
book 📘
book 📙
book 📖
book 📗
stick 🍡
ball 🍙
post 🏣
castle 🏯
decoration 🎍
flags 🎌
festival 🎎
tree 🎋
得 🉐
可 🉑
指 🈯
営 🈺
割 🈹
申 🈸
空 🈳
禁 🈲
月 🈷
有 🈶
満 🈵
合 🈴
サ 🈂
ココ 🈁
無 🈚
秘 ㊙
祝 ㊗
chevron 🔰
bless ⛪
bell 🔔
way 🌌
moon 🌗
waning 🌖
moon 🌔
moon 🌓
moon 🌒
moon 🌑
moon 🌙
moon 🌘
rays ☀
comet ☄
satellite 🛰
rockets 🚀
t-shirt 👕
fancy 👗
pouch 👝
trousers 👖
coin 👛
barefoot 👣
shirt 👔
swim 👙
prayer 📿
glasses 👓
kimono 👘
bags 🛍
trolley 🛒
prints 🐾
walking 🚶‍♀
walking 🚶
mysterious 👤
cut 💈
parlor 💇
haircut 💇‍♂
building 🏢
briefcase 💼
genderqueer 🏳‍🌈
gay 👨‍❤‍💋‍👨
anniversary 👨‍❤‍👨
anniversary 👩‍❤‍💋‍👩
wrestle 🤼‍♀
beacon 🚨
car 🚓
car 🚔
flag 📬
flag 📭
folder 📂
unlocked 🔓
classy 🧐
tree 🌴
umbrella 🏖
surfing 🏄‍♀
surfing 🏄
swimming 🏊
swimming 🏊‍♀
backpack 🎒
scooter 🛴
racquet 🎾
eye 👁
sound 👂
smells 👃
mouth 👄
tongue 👅
witness 👁‍🗨
eyes 🤪
sunglasses 🕶
publicaddress 📢
cheering 📣
volume 🔊
medium 🔉
sing 🎤
headphone 🎧
slash 🔕
volume 🔈
speaker 🔇
makeup 💄
index 📇
dividers 🗂
raised 🤚
button 🆙
flag 🏳
flag 🏴
cream 🍦
shaved 🍧
potato 🍠
wonka 🍭
pudding 🍮
ice 🍨
doughnut 🍩
chip 🍪
slice 🍰
cake 🎂
button 🆗
magic 🧙‍♀️
wizard 🧙‍♂️
box 🗃
genie 🧞‍♂️
genie 🧞‍♀️
shrimp 🍤
shellfish 🦐
seafood 🍢
sushi 🍣
box 🍱
soup 🍲
vegetable 🍅
hamburger 🍔
cheese 🍕
bowl 🍜
spaghetti 🍝
wheat 🍞
fries 🍟
cracker 🍘
rice 🍚
rice 🍛
peanut 🥜
kiwi 🥝
pancake 🥞
shallow 🥘
stuffed 🥙
egg 🥚
vegetable 🥔
carrot 🥕
baguette 🥖
salad 🥗
croissant 🥐
avocado 🥑
pickle 🥒
bacon 🥓
pie 🥧
sake 🍶
glass 🍷
up 🍳
skating ⛸
popping 🍾
glass 🍸
mug 🍺
mugs 🍻
bars 📶
chart 📊
porridge 🥣
hocho 🔪
tableware 🥄
leg 🍗
dagger 🗡
cup 🍵
milk 🥛
celebrate 🥂
hot ☕
beverage beverage
potable 🚰
glass 🔎
glass 🔍
scotch 🥃
shipping 📦
tray 📤
tray 📥
gift 🎁
off ☑
ballot 🗳
movie 🍿
projector 📽
clapper 🎬
camera 🎥
camera 🎦
frames 🎞
pineapple 🍍
toadstool 🍄
grapes 🍇
potassium 🍌
apple 🍏
melon 🍈
watermelon 🍉
c 🍊
sour 🍋
pear 🍐
peach 🍑
cherries 🍒
strawberry 🍓
eggplant 🍆
shamrock ☘
falling 🍁
leaf 🍂
wind 🍃
herb 🌿
tulip 🌷
rice 🌾
dandelion 🌼
sunflower 🌻
hibiscus 🌺
rosette 🏵
bouquet 💐
chime 🎐
shedding 🌳
heart 🧡
wedge 🧀
bone 🍖
meat 🥩
thanksgiving 🦃
delivery 🥡
kuaizi 🥢
springs ♨
sandwich 🥪
ball ⛹‍♀
bowl 🏈
baseball ⚾
ball ⚽
hoop 🏀
football 🏉
golfing 🏌
player ⛹
ball 🏌‍♀
Titania 🧚‍♀️
Puck 🧚‍♂️
racing 🏇
horse 🎠
chipmunk 🐿
dove 🕊
desert 🏜
island 🏝
garden 🏡
calendar 🗓
drink 🥤
non-potable 🚱
shower 🚿
closet 🚾
fleur-de-lis ⚜
car 🏎
motorcycle 🏍
weather 🌧
cloud 🌦
cloud 🌥
cloud 🌤
fog 🌫
whirlwind 🌪
lightning 🌩
snow 🌨
cloudy ⛅
thunderstorm ⛈
weather ☁
umbrella 🌂
ground ⛱
drops ☔
umbrella ☂
thermometer 🌡
typhoon 🌀
snowflake ❄
sunset 🌇
evening 🌆
mountains 🌄
night 🌉
wrap 🌯
taco 🌮
sausage 🌭
foggy 🌁
mountain 🏔
up 🧣
brr 🧥
snow ⛄
snowman ☃
skis 🎿
snowboarder 🏂
skier ⛷
toboggan 🛷
flower 💮
dying 🥀
increasing 📈
pepper 🌶
af 🔥
colada 🥥
tree 🌲
tree 🎄
almond 🌰
is 🏠
European 🏤
medicine 🏥
school 🏫
hotel 🏨
hotel 🏩
store 🏬
factory 🏭
castle 🏰
cityscape 🏙
climbing 🧗‍♀️
climbing 🧗‍♂️
mountain ⛰
biking 🚵‍♀
cableway 🚠
biking 🚵
railway 🚞
Australia 🌏
Americas 🌎
Europe 🌍
meridians 🌐
map 🗺
ceremony 🎑
sparkler 🎇
sparkle ❇
champion 🏆
button 🔆
crescent ☪
button ⏸
loop ➿
clock ⏰
stopwatch ⏱
clock ⏲
watch ⌚
clock 🕰
sand ⏳
sand ⌛
fireworks 🎆
frowning 🙍
pouting 🙎
sorry 🙇
pouting 🙎‍♂
frowning 🙍‍♂
bowing 🙇‍♀
relax 🧖‍♂️
room 🧖‍♀️
yogi 🧘‍♀️
position 🧘‍♂️
biking 🚴‍♀
bicycles 🚳
spinning 🚲
biking 🚴
hole ⛳
postal 📯
derelict 🏚
house 🏘
vaccinatoins 💉
vitamin 💊
staff ⚕
cover 📔
vehicle 🚌
bellhop 🛎
bed 🛏
bed 🛌
lamp 🛋
torch 🔦
light 🚥
light 🚦
candle 🕯
label 🏷
spanner 🔧
cutting ✂
chemistry ⚗
ship ⚓
pick ⚒
gear ⚙
mining ⛏
wrench 🛠
telescope 🔭
microscope 🔬
handgun 🔫
bolt 🔩
repairs 🔨
emblem 🔱
vice 🗜
swords ⚔
shield 🛡
weight 🏋
tramway 🚡
car 🚃
car 🚋
taxi 🚕
driving 🚗
sportutility 🚙
automobile 🚘
lorry 🚛
truck 🚚
classical 🏛
park 🏞
stadium 🏟
cross ✝
shrine ⛩
Buddhist ☸
yinyang ☯
cross ☦
worship 🛐
masjid 🕌
temple 🕍
candlestick 🕎
kaaba 🕋
Hindu 🕉
wish 🤲
videocassette 📼
tv 📺
tbt 📻
flash 📸
camera 📹
trip 📷
selfie 🤳
antenna 📡
phones 📵
vibration 📳
phone 📱
off 📴
paper 📰
flag 📫
machine 📠
receiver 📞
pager 📟
pencil 📝
telephone ☎
claim 🛄
entry ⛔
entry 🚫
smoking 🚭
littering 🚯
pedestrians 🚷
envelope 📨
rolled 🗞
scroll 📜
postbox 📮
flag 📪
letter 📧
book 📕
private 🔒
secure 🔐
letter ✉
terrestrial 🛸
list 📋
pencil ✏
badge 📛
ledger 📒
notebook 📓
pushpin 📌
pushpin 📍
Japan 🗾
calendar 📆
date 📅
up 📄
curl 📃
loop ➰
folder 📁
filing 🗄
symbol ☮
keyboard 🎹
plug 🔌
button 🅿
a 🅰
b 🅱
ab 🆎
button 🆕
identity 🆔
button 🆖
cl 🆑
button 🆓
button 🆒
vs 🆚
password 🔑
battery 🔋
stratocaster 🎸
violin 🎻
trumpet 🎺
saxophone 🎷
studio 🎙
knobs 🎛
slider 🎚
drumsticks 🥁
travel ✈
seat 💺
hashtag #⃣
pissed 🤬
way 🤯
heart 💔
celebration 🎀
reminder 🎗
spew 🤮
vampire ⚰
ashes ⚱
stub 🎫
tickets 🎟
tent 🎪
camping ⛺
wheel 🎡
roller 🎢
carp 🎏
award 🎖
Mrs. 🤶
oops 🤭
emoji 🤨
control 🛂
silver 🥈
third 🥉
gold 🥇
medal 🏅
hat 🧢
asterisk ✳
landing 🛬
departures 🛫
airplane 🛩
titanic 🚢
summer 🚤
copter 🚁
trains 🚂
subway 🚇
rightwards 🤜
leftwards 🤛
tick ✅
mark ✔
x ✖
button ❎
x ❌
Triton 🧜‍♂️
merwoman 🧜
weights 🏋‍♀
potsticker 🥟
glove 🥊
uniform 🥋
net 🥅
oil 🛢
convoluted 🥨
can 🥫
cabbage 🥦
quiet 🤫
sword 🤺
royalty 🤴
crossing 🚸
caution ⚠
ship 🛳
symbol ⚛
merwoman 🧜‍♀️
adult 🧑
bearded 🧔
kerchief 🧕
smart 🧠
stocking 🧦
camping 🏕
ferry ⛴
yacht ⛵
motorboat 🛥
canoe 🛶
hole 🕳
pump ⛽
dinosaur 🦕
rex 🦖
spiny 🦔
stripe 🦓
sign ☣
radioactive ☢
trolleybus 🚊
station 🚉
monorail 🚈
trolley 🚎
bus 🚍
van 🚐
ambulance 🚑
monorail 🚝
tractor 🚜
track 🛤
choo 🚆
suspension 🚟
road 🛣
motor 🛵
locker 🛅
customs 🛃
bath 🛀
bathtub 🛁
handicap ♿
symbol ♻
chain ⛓
prophecy 🥠
taxi 🚖
door 🚪
cigarette 🚬
litterbin 🚮
WC 🚻
toilet 🚽
engine 🚒
web 🕸
detective 🕵‍♀
spots 🦒
letters 🔤
〒♪&% 🔣
lowercase 🔡
uppercase 🔠
low 🔅
keycap10 🔟
registered ®
copyright ©
Liberty 🗽
Tokyo 🗼
wastebasket 🗑
"""


def create_map_emoji():
    # Split the input string into a list of lines
    lines = input_string.strip().split('\n')
    map_emojis = {}
    for line in lines:
        match = re.match(r"^([^\s]+)\s+(.*)", line)
        if match:
            key, value = match.groups()
            map_emojis[key] = value#.encode('utf-8')

    return map_emojis


map_emojis = create_map_emoji()
print(map_emojis,sep='\n')

def compara_com_emoji(parte):
    map_emojis = {'zero': '0⃣' , 'one': '1⃣', 'one-thirty': '🕜'}
    
    regex = '|'.join(map_emojis.values())
    output_list = re.split(regex, parte)
    output_list = list(filter(None,output_list))
    return output_list


parte = ' 0⃣ 62 9 9918-4004 1⃣ 62 3091-7324'
#map_emojis = testes.compara_com_emoji_fix(parte)

