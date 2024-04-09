import pygame
import animation # Import module animation

screen = pygame.display.set_mode((1200, 700))

# Dưới đây là tạo animation cho nhân vật, các thứ khác làm tương tự. (Chỉ cần gõ animaion. là có gợi ý về các loại)
# Một nhân vật sẽ có nhiều trạng thái, mỗi trạng thái sẽ gồm 1 list các ảnh, và mỗi ảnh sẽ được hiển thị theo thời gian.

knight_animation = animation.CharacterAnimation("knight_m") # Tạo animation cho knight.

knight_animation.update(pygame.time.get_ticks()) # Cập nhật animation

knight_animation.render(screen, position=(100, 100), hp=1, max_hp=1) # Hiển thị animation lên màn hình.

knight_animation.set_state("idle_anim_left") # chuyển sang trạng thái khác.

knight_animation.add_effect(animation.EffectAnimation("thunder", frame_speed=0.1, life_span=1)) # Thêm hiệu ứng cho nhân vật.
# Mỗi nhân vật khi bị tấn công sẽ có các hiệu ứng như chảy máu, cháy lửa, sét đánh, ...
# Sau khi thêm hiệu ứng thì khi chạy hết life_span sẽ tự động xóa hiệu ứng đó.

# Ngoài ra còn:
knight_animation.get_current_state() # Trả về tên trạng thái hiện tại của nhân vật.
knight_animation.get_height() # Trả về chiều cao của ảnh hiện tại
knight_animation.get_width() # Trả về chiều rộng của ảnh hiện tại
knight_animation.get_name() # Trả về tên của nhân vật

# Không được gọi các hàm, thuộc tính bắt đầu bằng "_" hoặc "__". Nếu cần thêm chức năng gì hãy liên hệ, tôi sẽ bổ sung