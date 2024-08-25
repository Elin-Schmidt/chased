def on_on_overlap(sprite, otherSprite):
    sprites.destroy(x, effects.fire, 1000)
    game.set_game_over_message(True, "Gottem!")
    game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

x: Sprite = None
game.splash("You're about to get chased!" "Get ready!")
mySprite = sprites.create(img("""
        . . . . . f f f f . . . . . 
            . . . f f 5 5 5 5 f f . . . 
            . . f 5 5 5 5 5 5 5 5 f . . 
            . f 5 5 5 5 5 5 5 5 5 5 f . 
            . f 5 5 5 d b b d 5 5 5 f . 
            f 5 5 5 b 4 4 4 4 b 5 5 5 f 
            f 5 5 c c 4 4 4 4 c c 5 5 f 
            f b b f b f 4 4 f b f b b f 
            f b b 4 1 f d d f 1 4 b b f 
            . f b f d d d d d d f b f . 
            . f e f e 4 4 4 4 e f e f . 
            . e 4 f 6 9 9 9 9 6 f 4 e . 
            . 4 d c 9 9 9 9 9 9 c d 4 . 
            . 4 f b 3 b 3 b 3 b b f 4 . 
            . . f f 3 b 3 b 3 3 f f . . 
            . . . . f f b b f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
tiles.place_on_random_tile(mySprite, sprites.dungeon.floor_dark2)
scene.camera_follow_sprite(mySprite)
x = sprites.create(img("""
        . . . . . . . . . . b 5 b . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . . . . b c . . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 d 1 f 5 5 d f . . 
            . . . . b 5 5 1 f f 5 d 4 c . . 
            . . . . b 5 5 d f b d d 4 4 . . 
            b d d d b b d 5 5 5 4 4 4 4 4 b 
            b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
            b d c 5 5 5 5 d 5 5 5 5 5 b . . 
            c d d c d 5 5 b 5 5 5 5 5 5 b . 
            c b d d c c b 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.enemy)
x2 = sprites.create(img("""
        . . f f f . . . . . . . . f f f 
            . f f c c . . . . . . f c b b c 
            f f c c . . . . . . f c b b c . 
            f c f c . . . . . . f b c c c . 
            f f f c c . c c . f c b b c c . 
            f f c 3 c c 3 c c f b c b b c . 
            f f b 3 b c 3 b c f b c c b c . 
            . c 1 b b b 1 b c b b c c c . . 
            . c 1 b b b 1 b b c c c c . . . 
            c b b b b b b b b b c c . . . . 
            c b 1 f f 1 c b b b b f . . . . 
            f f 1 f f 1 f b b b b f c . . . 
            f f 2 2 2 2 f b b b b f c c . . 
            . f 2 2 2 2 b b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . .
    """),
    SpriteKind.enemy)
x3 = sprites.create(img("""
        . . f f f . . . . . . . . f f f 
            . f f c c . . . . . . f c b b c 
            f f c c . . . . . . f c b b c . 
            f c f c . . . . . . f b c c c . 
            f f f c c . c c . f c b b c c . 
            f f c 3 c c 3 c c f b c b b c . 
            f f b 3 b c 3 b c f b c c b c . 
            . c 1 b b b 1 b c b b c c c . . 
            . c 1 b b b 1 b b c c c c . . . 
            c b b b b b b b b b c c . . . . 
            c b 1 f f 1 c b b b b f . . . . 
            f f 1 f f 1 f b b b b f c . . . 
            f f 2 2 2 2 f b b b b f c c . . 
            . f 2 2 2 2 b b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . .
    """),
    SpriteKind.enemy)
tiles.place_on_random_tile(x, sprites.dungeon.floor_light2)
info.set_score(info.score())

def on_forever():
    x.follow(mySprite, 70)
    info.change_score_by(1)
forever(on_forever)

def on_update_interval():
    tiles.place_on_random_tile(x2, sprites.dungeon.floor_light2)
    tiles.place_on_random_tile(x3, sprites.dungeon.floor_dark2)
game.on_update_interval(200, on_update_interval)
