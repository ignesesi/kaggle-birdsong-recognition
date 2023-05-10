import string
from pathlib import Path

class AUDIO_CONFIG:
    sampling_rate = 32000
    duration = 1
    hop_length = 251 # making it 128 in size
    fmin = 500
    fmax = 15000
    n_mels = 128
    n_fft = n_mels * 20
    samples = sampling_rate * duration
    padmode = 'reflect'
    
def fill_range(letter_start, letter_end, path_fill, dict_val={}):
    alphabet = list(string.ascii_lowercase)
    for a in alphabet[alphabet.index(letter_start):alphabet.index(letter_end)+1]:
        dict_val[a] = path_fill
    return dict_val

def get_dict_value(input_dir):
    dict_val = {}
    dict_val = fill_range('a','z',input_dir/"birdsong-resampled-train-audio-00",dict_val)
    # dict_val = fill_range('c','f',input_dir/"birdsong-resampled-train-audio-01",dict_val)
    # dict_val = fill_range('g','m',input_dir/"birdsong-resampled-train-audio-02",dict_val)
    # dict_val = fill_range('n','r',input_dir/"birdsong-resampled-train-audio-03",dict_val)
    # dict_val = fill_range('s','y',input_dir/"birdsong-resampled-train-audio-04",dict_val)
    return dict_val

BIRD_CODE = {
    'aldfly': 0, 'ameavo': 1, 'amebit': 2, 'amecro': 3, 'amegfi': 4,
    'amekes': 5, 'amepip': 6, 'amered': 7, 'amerob': 8, 'amewig': 9,
    'amewoo': 10, 'amtspa': 11, 'annhum': 12, 'astfly': 13, 'baisan': 14,
    'baleag': 15, 'balori': 16, 'banswa': 17, 'barswa': 18, 'bawwar': 19,
    'belkin1': 20, 'belspa2': 21, 'bewwre': 22, 'bkbcuc': 23, 'bkbmag1': 24,
    'bkbwar': 25, 'bkcchi': 26, 'bkchum': 27, 'bkhgro': 28, 'bkpwar': 29,
    'bktspa': 30, 'blkpho': 31, 'blugrb1': 32, 'blujay': 33, 'bnhcow': 34,
    'boboli': 35, 'bongul': 36, 'brdowl': 37, 'brebla': 38, 'brespa': 39,
    'brncre': 40, 'brnthr': 41, 'brthum': 42, 'brwhaw': 43, 'btbwar': 44,
    'btnwar': 45, 'btywar': 46, 'buffle': 47, 'buggna': 48, 'buhvir': 49,
    'bulori': 50, 'bushti': 51, 'buwtea': 52, 'buwwar': 53, 'cacwre': 54,
    #'calgul': 55, 'calqua': 56, 'camwar': 57, 'cangoo': 58, 'canwar': 59,
    # 'canwre': 60, 'carwre': 61, 'casfin': 62, 'caster1': 63, 'casvir': 64,
    # 'cedwax': 65, 'chispa': 66, 'chiswi': 67, 'chswar': 68, 'chukar': 69,
    # 'clanut': 70, 'cliswa': 71, 'comgol': 72, 'comgra': 73, 'comloo': 74,
    # 'commer': 75, 'comnig': 76, 'comrav': 77, 'comred': 78, 'comter': 79,
    # 'comyel': 80, 'coohaw': 81, 'coshum': 82, 'cowscj1': 83, 'daejun': 84,
    # 'doccor': 85, 'dowwoo': 86, 'dusfly': 87, 'eargre': 88, 'easblu': 89,
    # 'easkin': 90, 'easmea': 91, 'easpho': 92, 'eastow': 93, 'eawpew': 94,
    # 'eucdov': 95, 'eursta': 96, 'evegro': 97, 'fiespa': 98, 'fiscro': 99,
    # 'foxspa': 100, 'gadwal': 101, 'gcrfin': 102, 'gnttow': 103, 'gnwtea': 104,
    # 'gockin': 105, 'gocspa': 106, 'goleag': 107, 'grbher3': 108, 'grcfly': 109,
    # 'greegr': 110, 'greroa': 111, 'greyel': 112, 'grhowl': 113, 'grnher': 114,
    # 'grtgra': 115, 'grycat': 116, 'gryfly': 117, 'haiwoo': 118, 'hamfly': 119,
    # 'hergul': 120, 'herthr': 121, 'hoomer': 122, 'hoowar': 123, 'horgre': 124,
    # 'horlar': 125, 'houfin': 126, 'houspa': 127, 'houwre': 128, 'indbun': 129,
    # 'juntit1': 130, 'killde': 131, 'labwoo': 132, 'larspa': 133, 'lazbun': 134,
    # 'leabit': 135, 'leafly': 136, 'leasan': 137, 'lecthr': 138, 'lesgol': 139,
    # 'lesnig': 140, 'lesyel': 141, 'lewwoo': 142, 'linspa': 143, 'lobcur': 144,
    # 'lobdow': 145, 'logshr': 146, 'lotduc': 147, 'louwat': 148, 'macwar': 149,
    # 'magwar': 150, 'mallar3': 151, 'marwre': 152, 'merlin': 153, 'moublu': 154,
    # 'mouchi': 155, 'moudov': 156, 'norcar': 157, 'norfli': 158, 'norhar2': 159,
    # 'normoc': 160, 'norpar': 161, 'norpin': 162, 'norsho': 163, 'norwat': 164,
    # 'nrwswa': 165, 'nutwoo': 166, 'olsfly': 167, 'orcwar': 168, 'osprey': 169,
    # 'ovenbi1': 170, 'palwar': 171, 'pasfly': 172, 'pecsan': 173, 'perfal': 174,
    # 'phaino': 175, 'pibgre': 176, 'pilwoo': 177, 'pingro': 178, 'pinjay': 179,
    # 'pinsis': 180, 'pinwar': 181, 'plsvir': 182, 'prawar': 183, 'purfin': 184,
    # 'pygnut': 185, 'rebmer': 186, 'rebnut': 187, 'rebsap': 188, 'rebwoo': 189,
    # 'redcro': 190, 'redhea': 191, 'reevir1': 192, 'renpha': 193, 'reshaw': 194,
    # 'rethaw': 195, 'rewbla': 196, 'ribgul': 197, 'rinduc': 198, 'robgro': 199,
    # 'rocpig': 200, 'rocwre': 201, 'rthhum': 202, 'ruckin': 203, 'rudduc': 204,
    # 'rufgro': 205, 'rufhum': 206, 'rusbla': 207, 'sagspa1': 208, 'sagthr': 209,
    # 'savspa': 210, 'saypho': 211, 'scatan': 212, 'scoori': 213, 'semplo': 214,
    # 'semsan': 215, 'sheowl': 216, 'shshaw': 217, 'snobun': 218, 'snogoo': 219,
    # 'solsan': 220, 'sonspa': 221, 'sora': 222, 'sposan': 223, 'spotow': 224,
    # 'stejay': 225, 'swahaw': 226, 'swaspa': 227, 'swathr': 228, 'treswa': 229,
    # 'truswa': 230, 'tuftit': 231, 'tunswa': 232, 'veery': 233, 'vesspa': 234,
    # 'vigswa': 235, 'warvir': 236, 'wesblu': 237, 'wesgre': 238, 'weskin': 239,
    # 'wesmea': 240, 'wessan': 241, 'westan': 242, 'wewpew': 243, 'whbnut': 244,
    # 'whcspa': 245, 'whfibi': 246, 'whtspa': 247, 'whtswi': 248, 'wilfly': 249,
    # 'wilsni1': 250, 'wiltur': 251, 'winwre3': 252, 'wlswar': 253, 'wooduc': 254,
    # 'wooscj2': 255, 'woothr': 256, 'y00475': 257, 'yebfly': 258, 'yebsap': 259,
    # 'yehbla': 260, 'yelwar': 261, 'yerwar': 262, 'yetvir': 263
}

EBIRD_LABEL = {'aldfly': 'Empidonax alnorum_Alder Flycatcher',
 'ameavo': 'Recurvirostra americana_American Avocet',
 'amebit': 'Botaurus lentiginosus_American Bittern',
 'amecro': 'Corvus brachyrhynchos_American Crow',
 'amegfi': 'Spinus tristis_American Goldfinch',
 'amekes': 'Falco sparverius_American Kestrel',
 'amepip': 'Anthus rubescens_American Pipit',
 'amered': 'Setophaga ruticilla_American Redstart',
 'amerob': 'Turdus migratorius_American Robin',
 'amewig': 'Mareca americana_American Wigeon',
 'amewoo': 'Scolopax minor_American Woodcock',
 'amtspa': 'Spizelloides arborea_American Tree Sparrow',
 'annhum': "Calypte anna_Anna's Hummingbird",
 'astfly': 'Myiarchus cinerascens_Ash-throated Flycatcher',
 'baisan': "Calidris bairdii_Baird's Sandpiper",
 'baleag': 'Haliaeetus leucocephalus_Bald Eagle',
 'balori': 'Icterus galbula_Baltimore Oriole',
 'banswa': 'Riparia riparia_Bank Swallow',
 'barswa': 'Hirundo rustica_Barn Swallow',
 'bawwar': 'Mniotilta varia_Black-and-white Warbler',
 'belkin1': 'Megaceryle alcyon_Belted Kingfisher',
 'belspa2': "Artemisiospiza belli_Bell's Sparrow",
 'bewwre': "Thryomanes bewickii_Bewick's Wren",
 'bkbcuc': 'Coccyzus erythropthalmus_Black-billed Cuckoo',
 'bkbmag1': 'Pica hudsonia_Black-billed Magpie',
 'bkbwar': 'Setophaga fusca_Blackburnian Warbler',
 'bkcchi': 'Poecile atricapillus_Black-capped Chickadee',
 'bkchum': 'Archilochus alexandri_Black-chinned Hummingbird',
 'bkhgro': 'Pheucticus melanocephalus_Black-headed Grosbeak',
 'bkpwar': 'Setophaga striata_Blackpoll Warbler',
 'bktspa': 'Amphispiza bilineata_Black-throated Sparrow',
 'blkpho': 'Sayornis nigricans_Black Phoebe',
 'blugrb1': 'Passerina caerulea_Blue Grosbeak',
 'blujay': 'Cyanocitta cristata_Blue Jay',
 'bnhcow': 'Molothrus ater_Brown-headed Cowbird',
 'boboli': 'Dolichonyx oryzivorus_Bobolink',
 'bongul': "Chroicocephalus philadelphia_Bonaparte's Gull",
 'brdowl': 'Strix varia_Barred Owl',
 'brebla': "Euphagus cyanocephalus_Brewer's Blackbird",
 'brespa': "Spizella breweri_Brewer's Sparrow",
 'brncre': 'Certhia americana_Brown Creeper',
 'brnthr': 'Toxostoma rufum_Brown Thrasher',
 'brthum': 'Selasphorus platycercus_Broad-tailed Hummingbird',
 'brwhaw': 'Buteo platypterus_Broad-winged Hawk',
 'btbwar': 'Setophaga caerulescens_Black-throated Blue Warbler',
 'btnwar': 'Setophaga virens_Black-throated Green Warbler',
 'btywar': 'Setophaga nigrescens_Black-throated Gray Warbler',
 'buffle': 'Bucephala albeola_Bufflehead',
 'buggna': 'Polioptila caerulea_Blue-gray Gnatcatcher',
 'buhvir': 'Vireo solitarius_Blue-headed Vireo',
 'bulori': "Icterus bullockii_Bullock's Oriole",
 'bushti': 'Psaltriparus minimus_Bushtit',
 'buwtea': 'Spatula discors_Blue-winged Teal',
 'buwwar': 'Vermivora cyanoptera_Blue-winged Warbler',
 'cacwre': 'Campylorhynchus brunneicapillus_Cactus Wren',
 # 'calgul': 'Larus californicus_California Gull',
 # 'calqua': 'Callipepla californica_California Quail',
 # 'camwar': 'Setophaga tigrina_Cape May Warbler',
 # 'cangoo': 'Branta canadensis_Canada Goose',
 # 'canwar': 'Cardellina canadensis_Canada Warbler',
 # 'canwre': 'Catherpes mexicanus_Canyon Wren',
 # 'carwre': 'Thryothorus ludovicianus_Carolina Wren',
 # 'casfin': "Haemorhous cassinii_Cassin's Finch",
 # 'caster1': 'Hydroprogne caspia_Caspian Tern',
 # 'casvir': "Vireo cassinii_Cassin's Vireo",
 # 'cedwax': 'Bombycilla cedrorum_Cedar Waxwing',
 # 'chispa': 'Spizella passerina_Chipping Sparrow',
 # 'chiswi': 'Chaetura pelagica_Chimney Swift',
 # 'chswar': 'Setophaga pensylvanica_Chestnut-sided Warbler',
 # 'chukar': 'Alectoris chukar_Chukar',
 # 'clanut': "Nucifraga columbiana_Clark's Nutcracker",
 # 'cliswa': 'Petrochelidon pyrrhonota_Cliff Swallow',
 # 'comgol': 'Bucephala clangula_Common Goldeneye',
 # 'comgra': 'Quiscalus quiscula_Common Grackle',
 # 'comloo': 'Gavia immer_Common Loon',
 # 'commer': 'Mergus merganser_Common Merganser',
 # 'comnig': 'Chordeiles minor_Common Nighthawk',
 # 'comrav': 'Corvus corax_Common Raven',
 # 'comred': 'Acanthis flammea_Common Redpoll',
 # 'comter': 'Sterna hirundo_Common Tern',
 # 'comyel': 'Geothlypis trichas_Common Yellowthroat',
 # 'coohaw': "Accipiter cooperii_Cooper's Hawk",
 # 'coshum': "Calypte costae_Costa's Hummingbird",
 # 'cowscj1': 'Aphelocoma californica_California Scrub-Jay',
 # 'daejun': 'Junco hyemalis_Dark-eyed Junco',
 # 'doccor': 'Phalacrocorax auritus_Double-crested Cormorant',
 # 'dowwoo': 'Dryobates pubescens_Downy Woodpecker',
 # 'dusfly': 'Empidonax oberholseri_Dusky Flycatcher',
 # 'eargre': 'Podiceps nigricollis_Eared Grebe',
 # 'easblu': 'Sialia sialis_Eastern Bluebird',
 # 'easkin': 'Tyrannus tyrannus_Eastern Kingbird',
 # 'easmea': 'Sturnella magna_Eastern Meadowlark',
 # 'easpho': 'Sayornis phoebe_Eastern Phoebe',
 # 'eastow': 'Pipilo erythrophthalmus_Eastern Towhee',
 # 'eawpew': 'Contopus virens_Eastern Wood-Pewee',
 # 'eucdov': 'Streptopelia decaocto_Eurasian Collared-Dove',
 # 'eursta': 'Sturnus vulgaris_European Starling',
 # 'evegro': 'Coccothraustes vespertinus_Evening Grosbeak',
 # 'fiespa': 'Spizella pusilla_Field Sparrow',
 # 'fiscro': 'Corvus ossifragus_Fish Crow',
 # 'foxspa': 'Passerella iliaca_Fox Sparrow',
 # 'gadwal': 'Mareca strepera_Gadwall',
 # 'gcrfin': 'Leucosticte tephrocotis_Gray-crowned Rosy-Finch',
 # 'gnttow': 'Pipilo chlorurus_Green-tailed Towhee',
 # 'gnwtea': 'Anas crecca_Green-winged Teal',
 # 'gockin': 'Regulus satrapa_Golden-crowned Kinglet',
 # 'gocspa': 'Zonotrichia atricapilla_Golden-crowned Sparrow',
 # 'goleag': 'Aquila chrysaetos_Golden Eagle',
 # 'grbher3': 'Ardea herodias_Great Blue Heron',
 # 'grcfly': 'Myiarchus crinitus_Great Crested Flycatcher',
 # 'greegr': 'Ardea alba_Great Egret',
 # 'greroa': 'Geococcyx californianus_Greater Roadrunner',
 # 'greyel': 'Tringa melanoleuca_Greater Yellowlegs',
 # 'grhowl': 'Bubo virginianus_Great Horned Owl',
 # 'grnher': 'Butorides virescens_Green Heron',
 # 'grtgra': 'Quiscalus mexicanus_Great-tailed Grackle',
 # 'grycat': 'Dumetella carolinensis_Gray Catbird',
 # 'gryfly': 'Empidonax wrightii_Gray Flycatcher',
 # 'haiwoo': 'Dryobates villosus_Hairy Woodpecker',
 # 'hamfly': "Empidonax hammondii_Hammond's Flycatcher",
 # 'hergul': 'Larus argentatus_Herring Gull',
 # 'herthr': 'Catharus guttatus_Hermit Thrush',
 # 'hoomer': 'Lophodytes cucullatus_Hooded Merganser',
 # 'hoowar': 'Setophaga citrina_Hooded Warbler',
 # 'horgre': 'Podiceps auritus_Horned Grebe',
 # 'horlar': 'Eremophila alpestris_Horned Lark',
 # 'houfin': 'Haemorhous mexicanus_House Finch',
 # 'houspa': 'Passer domesticus_House Sparrow',
 # 'houwre': 'Troglodytes aedon_House Wren',
 # 'indbun': 'Passerina cyanea_Indigo Bunting',
 # 'juntit1': 'Baeolophus ridgwayi_Juniper Titmouse',
 # 'killde': 'Charadrius vociferus_Killdeer',
 # 'labwoo': 'Dryobates scalaris_Ladder-backed Woodpecker',
 # 'larspa': 'Chondestes grammacus_Lark Sparrow',
 # 'lazbun': 'Passerina amoena_Lazuli Bunting',
 # 'leabit': 'Ixobrychus exilis_Least Bittern',
 # 'leafly': 'Empidonax minimus_Least Flycatcher',
 # 'leasan': 'Calidris minutilla_Least Sandpiper',
 # 'lecthr': "Toxostoma lecontei_LeConte's Thrasher",
 # 'lesgol': 'Spinus psaltria_Lesser Goldfinch',
 # 'lesnig': 'Chordeiles acutipennis_Lesser Nighthawk',
 # 'lesyel': 'Tringa flavipes_Lesser Yellowlegs',
 # 'lewwoo': "Melanerpes lewis_Lewis's Woodpecker",
 # 'linspa': "Melospiza lincolnii_Lincoln's Sparrow",
 # 'lobcur': 'Numenius americanus_Long-billed Curlew',
 # 'lobdow': 'Limnodromus scolopaceus_Long-billed Dowitcher',
 # 'logshr': 'Lanius ludovicianus_Loggerhead Shrike',
 # 'lotduc': 'Clangula hyemalis_Long-tailed Duck',
 # 'louwat': 'Parkesia motacilla_Louisiana Waterthrush',
 # 'macwar': "Geothlypis tolmiei_MacGillivray's Warbler",
 # 'magwar': 'Setophaga magnolia_Magnolia Warbler',
 # 'mallar3': 'Anas platyrhynchos_Mallard',
 # 'marwre': 'Cistothorus palustris_Marsh Wren',
 # 'merlin': 'Falco columbarius_Merlin',
 # 'moublu': 'Sialia currucoides_Mountain Bluebird',
 # 'mouchi': 'Poecile gambeli_Mountain Chickadee',
 # 'moudov': 'Zenaida macroura_Mourning Dove',
 # 'norcar': 'Cardinalis cardinalis_Northern Cardinal',
 # 'norfli': 'Colaptes auratus_Northern Flicker',
 # 'norhar2': 'Circus hudsonius_Northern Harrier',
 # 'normoc': 'Mimus polyglottos_Northern Mockingbird',
 # 'norpar': 'Setophaga americana_Northern Parula',
 # 'norpin': 'Anas acuta_Northern Pintail',
 # 'norsho': 'Spatula clypeata_Northern Shoveler',
 # 'norwat': 'Parkesia noveboracensis_Northern Waterthrush',
 # 'nrwswa': 'Stelgidopteryx serripennis_Northern Rough-winged Swallow',
 # 'nutwoo': "Dryobates nuttallii_Nuttall's Woodpecker",
 # 'olsfly': 'Contopus cooperi_Olive-sided Flycatcher',
 # 'orcwar': 'Leiothlypis celata_Orange-crowned Warbler',
 # 'osprey': 'Pandion haliaetus_Osprey',
 # 'ovenbi1': 'Seiurus aurocapilla_Ovenbird',
 # 'palwar': 'Setophaga palmarum_Palm Warbler',
 # 'pasfly': 'Empidonax difficilis_Pacific-slope Flycatcher',
 # 'pecsan': 'Calidris melanotos_Pectoral Sandpiper',
 # 'perfal': 'Falco peregrinus_Peregrine Falcon',
 # 'phaino': 'Phainopepla nitens_Phainopepla',
 # 'pibgre': 'Podilymbus podiceps_Pied-billed Grebe',
 # 'pilwoo': 'Dryocopus pileatus_Pileated Woodpecker',
 # 'pingro': 'Pinicola enucleator_Pine Grosbeak',
 # 'pinjay': 'Gymnorhinus cyanocephalus_Pinyon Jay',
 # 'pinsis': 'Spinus pinus_Pine Siskin',
 # 'pinwar': 'Setophaga pinus_Pine Warbler',
 # 'plsvir': 'Vireo plumbeus_Plumbeous Vireo',
 # 'prawar': 'Setophaga discolor_Prairie Warbler',
 # 'purfin': 'Haemorhous purpureus_Purple Finch',
 # 'pygnut': 'Sitta pygmaea_Pygmy Nuthatch',
 # 'rebmer': 'Mergus serrator_Red-breasted Merganser',
 # 'rebnut': 'Sitta canadensis_Red-breasted Nuthatch',
 # 'rebsap': 'Sphyrapicus ruber_Red-breasted Sapsucker',
 # 'rebwoo': 'Melanerpes carolinus_Red-bellied Woodpecker',
 # 'redcro': 'Loxia curvirostra_Red Crossbill',
 # 'redhea': 'Aythya americana_Redhead',
 # 'reevir1': 'Vireo olivaceus_Red-eyed Vireo',
 # 'renpha': 'Phalaropus lobatus_Red-necked Phalarope',
 # 'reshaw': 'Buteo lineatus_Red-shouldered Hawk',
 # 'rethaw': 'Buteo jamaicensis_Red-tailed Hawk',
 # 'rewbla': 'Agelaius phoeniceus_Red-winged Blackbird',
 # 'ribgul': 'Larus delawarensis_Ring-billed Gull',
 # 'rinduc': 'Aythya collaris_Ring-necked Duck',
 # 'robgro': 'Pheucticus ludovicianus_Rose-breasted Grosbeak',
 # 'rocpig': 'Columba livia_Rock Pigeon',
 # 'rocwre': 'Salpinctes obsoletus_Rock Wren',
 # 'rthhum': 'Archilochus colubris_Ruby-throated Hummingbird',
 # 'ruckin': 'Regulus calendula_Ruby-crowned Kinglet',
 # 'rudduc': 'Oxyura jamaicensis_Ruddy Duck',
 # 'rufgro': 'Bonasa umbellus_Ruffed Grouse',
 # 'rufhum': 'Selasphorus rufus_Rufous Hummingbird',
 # 'rusbla': 'Euphagus carolinus_Rusty Blackbird',
 # 'sagspa1': 'Artemisiospiza nevadensis_Sagebrush Sparrow',
 # 'sagthr': 'Oreoscoptes montanus_Sage Thrasher',
 # 'savspa': 'Passerculus sandwichensis_Savannah Sparrow',
 # 'saypho': "Sayornis saya_Say's Phoebe",
 # 'scatan': 'Piranga olivacea_Scarlet Tanager',
 # 'scoori': "Icterus parisorum_Scott's Oriole",
 # 'semplo': 'Charadrius semipalmatus_Semipalmated Plover',
 # 'semsan': 'Calidris pusilla_Semipalmated Sandpiper',
 # 'sheowl': 'Asio flammeus_Short-eared Owl',
 # 'shshaw': 'Accipiter striatus_Sharp-shinned Hawk',
 # 'snobun': 'Plectrophenax nivalis_Snow Bunting',
 # 'snogoo': 'Anser caerulescens_Snow Goose',
 # 'solsan': 'Tringa solitaria_Solitary Sandpiper',
 # 'sonspa': 'Melospiza melodia_Song Sparrow',
 # 'sora': 'Porzana carolina_Sora',
 # 'sposan': 'Actitis macularius_Spotted Sandpiper',
 # 'spotow': 'Pipilo maculatus_Spotted Towhee',
 # 'stejay': "Cyanocitta stelleri_Steller's Jay",
 # 'swahaw': "Buteo swainsoni_Swainson's Hawk",
 # 'swaspa': 'Melospiza georgiana_Swamp Sparrow',
 # 'swathr': "Catharus ustulatus_Swainson's Thrush",
 # 'treswa': 'Tachycineta bicolor_Tree Swallow',
 # 'truswa': 'Cygnus buccinator_Trumpeter Swan',
 # 'tuftit': 'Baeolophus bicolor_Tufted Titmouse',
 # 'tunswa': 'Cygnus columbianus_Tundra Swan',
 # 'veery': 'Catharus fuscescens_Veery',
 # 'vesspa': 'Pooecetes gramineus_Vesper Sparrow',
 # 'vigswa': 'Tachycineta thalassina_Violet-green Swallow',
 # 'warvir': 'Vireo gilvus_Warbling Vireo',
 # 'wesblu': 'Sialia mexicana_Western Bluebird',
 # 'wesgre': 'Aechmophorus occidentalis_Western Grebe',
 # 'weskin': 'Tyrannus verticalis_Western Kingbird',
 # 'wesmea': 'Sturnella neglecta_Western Meadowlark',
 # 'wessan': 'Calidris mauri_Western Sandpiper',
 # 'westan': 'Piranga ludoviciana_Western Tanager',
 # 'wewpew': 'Contopus sordidulus_Western Wood-Pewee',
 # 'whbnut': 'Sitta carolinensis_White-breasted Nuthatch',
 # 'whcspa': 'Zonotrichia leucophrys_White-crowned Sparrow',
 # 'whfibi': 'Plegadis chihi_White-faced Ibis',
 # 'whtspa': 'Zonotrichia albicollis_White-throated Sparrow',
 # 'whtswi': 'Aeronautes saxatalis_White-throated Swift',
 # 'wilfly': 'Empidonax traillii_Willow Flycatcher',
 # 'wilsni1': "Gallinago delicata_Wilson's Snipe",
 # 'wiltur': 'Meleagris gallopavo_Wild Turkey',
 # 'winwre3': 'Troglodytes hiemalis_Winter Wren',
 # 'wlswar': "Cardellina pusilla_Wilson's Warbler",
 # 'wooduc': 'Aix sponsa_Wood Duck',
 # 'wooscj2': "Aphelocoma woodhouseii_Woodhouse's Scrub-Jay",
 # 'woothr': 'Hylocichla mustelina_Wood Thrush',
 # 'y00475': 'Fulica americana_American Coot',
 # 'yebfly': 'Empidonax flaviventris_Yellow-bellied Flycatcher',
 # 'yebsap': 'Sphyrapicus varius_Yellow-bellied Sakpsucker',
 # 'yehbla': 'Xanthocephalus xanthocephalus_Yellow-headed Blackbird',
 # 'yelwar': 'Setophaga petechia_Yellow Warbler',
 # 'yerwar': 'Setophaga coronata_Yellow-rumped Warbler',
 # 'yetvir': 'Vireo flavifrons_Yellow-throated Vireo'
}

INV_EBIRD_LABEL = {v: k for k, v in EBIRD_LABEL.items()}