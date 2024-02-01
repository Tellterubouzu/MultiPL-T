# need to give deepspeed config file as argument
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Please give deepspeed config file as argument"
    exit 1
fi
python3 -m torch.distributed.launch \
        --nproc_per_node 8 \
        main.py \
        --deepspeed="$1" \
        --model_path="bigcode/starcoder2-3b-new-impl" \
        --model_revision="lcft" \
        --dataset_name="nuprl-staging/multipl-t-mixed-deduped" \
        --no_approx_tokens \
        --output_dir="./model_starcoder2_3b_mix_v2" \
        --seq_length 2048 \
        --epochs 6 \
        --batch_size 1 \
        --gradient_accumulation_steps 4 \
        --learning_rate 2e-5 \
        --num_warmup_steps 10 \
        --num_workers=$(expr $(nproc --all) - 4) \
        --no_fp16 \
        --bf16 \
        --torch_dtype "bfloat16" \
        --eval_freq 0 \
        --perc_valid_set 0.0 \
        --save_total_limit 20
