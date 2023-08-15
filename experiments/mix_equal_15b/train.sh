# need to give deepspeed config file as argument
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Please give deepspeed config file as argument"
    exit 1
fi
python3 -m torch.distributed.launch \
        --nproc_per_node 8 \
        train.py \
        --deepspeed="$1" \
        --model_path="bigcode/starcoderbase" \
        --no_custom_tokenizer \
        --dataset_name="nuprl/multiplt_all_lang_equal_aug" \
        --no_approx_tokens \
        --output_dir="./model_starcoder15b_all_lang_equal_paper" \
        --seq_length 2048 \
        --epochs 10 \
        --batch_size 1 \
        --gradient_accumulation_steps 4 \
        --learning_rate 2e-5 \
        --num_warmup_steps 10 \
        --num_workers=$(expr $(nproc --all) - 4) \
        --no_fp16 \
        --bf16 \
        --perc_valid_set 0.0025 \
        --save_total_limit 20
