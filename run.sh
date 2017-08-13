# Iterative with random pos
python agent_test.py \
  -repeat 10 \
  -logs \
  -time_limit inf \
  -p2_type alphabeta \
  -p2_iterative \
  -p2_depth 10 \
  -p1_type alphabeta \
  -p1_iterative \
  -p1_depth 10 \
  -write \
  -name_date \
  -name random_pos_game

# flipped
python agent_test.py \
  -repeat 10 \
  -logs \
  -time_limit inf \
  -p1_type alphabeta \
  -p1_iterative \
  -p1_depth 10 \
  -p2_type alphabeta \
  -p2_iterative \
  -p2_depth 10 \
  -write \
  -name_date \
  -name random_pos_game
